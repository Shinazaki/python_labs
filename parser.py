import requests as rq
from bs4 import BeautifulSoup
from env import URL

response = rq.get(URL)
bs = BeautifulSoup(response.text, "lxml")

events = bs.find_all("li", "gu24-event events-afisha-li")

all_prices = []        
events_with_prices = []  
places_count = {}       
with open("afisha.txt", "w", encoding="utf-8") as file:
    for event in events:
        event_name = event.find("p", "gu24-event__name")
        event_price = event.find("span", "additional-button prices-bottom")
        event_age_rate = event.find("span", "additional-button min-age-button")
        event_url = event.find("a")

        if event_name and event_url:
            name = event_name.text.strip()

            movie_url = event_url["href"]
            movie_id = movie_url.split("/")[-1].split("-")[0]

            if event_age_rate:
                age_rate = event_age_rate.text.strip()
            else:
                age_rate = "Нет возрастного ограничения"

            if event_price:
                price = event_price.get_text(" ", strip=True)

                cleaned = ""
                for ch in price:
                    if ch.isdigit() or ch in ".,":
                        cleaned += "." if ch == "," else ch
                    else:
                        cleaned += " "

                for part in cleaned.split():
                    part = part.strip(".")
                    if part:
                        num = float(part)
                        all_prices.append(num)
                        events_with_prices.append((num, name))
            else:
                price = "Нет ценника"

            api_url = f"https://api.24afisha.by/api/v2/schedule/events/{movie_id}"
            payload = {
                "cityId": 3
            }

            movie_response = rq.get(api_url, params=payload)
            json_data = movie_response.json()
            places_and_dates = []

            if json_data.get("data"):
                movie_info = json_data["data"][0]
                objects = movie_info["objects"]

                for i in range(len(objects)):
                    place = objects[i].get("name")
                    if place:
                        places_count[place] = places_count.get(place, 0) + 1

                    sessions = objects[i]["sessions"]
                    date_and_time = []
                    for i in range(len(sessions)):
                        date = sessions[i].get("dateStr")
                        time = sessions[i].get("timeStr")
                        date_and_time.append([date, time])
                    places_and_dates.append([place, date_and_time])

            lines = [
                "=" * 50,
                f"🎬 {name} ({age_rate})",
                f"💰 Цена: {price}",
                "-" * 50,
            ]

            if places_and_dates:
                for place, sessions in places_and_dates:
                    lines.append(f"📍 {place}:")
                    grouped_dates = {}
                    for date, time in sessions:
                        grouped_dates.setdefault(date, []).append(time)

                    for date, times in grouped_dates.items():
                        lines.append(f"   📅 {date}: {', '.join(times)}")
            else:
                lines.append("   Сеансов пока нет")

            lines.append("=" * 50 + "\n")

            result = "\n".join(lines)
            print(result)
            file.write(result + "\n")

    stats_lines = [
        "#" * 50,
        "📊 ИТОГОВАЯ СТАТИСТИКА ПО РАЗДЕЛУ",
        "#" * 50,
    ]

    if all_prices:
        min_price = min(all_prices)
        max_price = max(all_prices)
        avg_price = sum(all_prices) / len(all_prices)

        cheapest_event = min(events_with_prices, key=lambda x: x[0])
        most_expensive_event = max(events_with_prices, key=lambda x: x[0])

        stats_lines.extend([
            f"💵 Минимальная стоимость билета: {min_price:.2f} руб.",
            f"💸 Максимальная стоимость билета: {max_price:.2f} руб.",
            f"📈 Средняя стоимость билета: {avg_price:.2f} руб.",
            "-" * 50,
            f"🏷 Самый дешёвый билет: «{cheapest_event[1]}» ({cheapest_event[0]:.2f} руб.)",
            f"💎 Самый дорогой билет: «{most_expensive_event[1]}» ({most_expensive_event[0]:.2f} руб.)",
        ])
    else:
        stats_lines.append("Цены на билеты в данном разделе не найдены.")

    if places_count:
        busiest_place = max(places_count.items(), key=lambda x: x[1])
        stats_lines.extend([
            "-" * 50,
            f"🏟 Самая загруженная площадка: {busiest_place[0]} (мероприятий: {busiest_place[1]})",
        ])
    else:
        stats_lines.append("Данные о площадках не найдены.")

    stats_lines.append("#" * 50)

    stats_output = "\n".join(stats_lines)
    print(stats_output)
    file.write(stats_output + "\n")