import requests
from bs4 import BeautifulSoup
import csv

def get_animals_count_by_letter(url):
    animals_count = {}
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Находим все категории животных на странице
        category_groups = soup.select('.mw-category-group')
        for group in category_groups:
            header = group.find('h3').get_text(strip=True)
            count = len(group.find_all('li'))
            animals_count[header[0]] = animals_count.get(header[0], 0) + count

        # Ищем ссылку на следующую страницу категорий
        next_link = soup.find('a', string='Следующая страница')
        url = next_link['href'] if next_link else None
        if url:
            url = f"https://ru.wikipedia.org{url}"  # Формируем полный URL
            print(f'Перешли по {url}')

    return animals_count

def save_to_csv(data, filename):
    # Сохраняем данные в CSV-файл
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for letter, count in sorted(data.items()):
            writer.writerow([letter, count])

def main():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    animals_count = get_animals_count_by_letter(url)
    save_to_csv(animals_count, 'beasts.csv')

if __name__ == "__main__":
    main()
