
import requests

ANIMAL_FILE = "animals.html"

def get_user_input():
    """ Get the user input for a chosen animal"""
    animal = input("\nEnter the name of an animal: ").strip().lower()
    return animal


def load_data(animal):
    """ Load data from Animals API"""
    ANIMAL = animal
    url = f"https://api.api-ninjas.com/v1/animals?name={ANIMAL}"
    params = {"X-Api-Key": "sqxq+uQNGhWNlbY7oYFbmg==hYHrc0liP2QMeFKH"}

    response = requests.get(url, params=params)
    if response.status_code == 200 and response.json() != []:
        data = response.json()
        return data
    else:
        print("Response code:", response.status_code)
        print(f"Animal {ANIMAL} NOT found")
        no_such_animal = [ANIMAL]  ### CHECK IF WORKING
        return no_such_animal


def read_html(file_name):
    """
       read a html file
    """
    with open(file_name, "r", encoding="utf-8") as handle:
        html_text = handle.read()
        return html_text


def write_html(html_text, file_name):
    """
    write a html file
    """
    with open(file_name, "w", encoding="utf-8") as h:
        h.write(html_text)
        print(f"Website was successful generated to the file {file_name}")


def generate_string(animals_data):
    if len(animals_data) == 1:
        no_output = f"<h2>The animal {animals_data[0]} doesn't exist.</h2>"
        return no_output
    output = ""     # define empty string
    for animal in animals_data:
        # append info to each string of info
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal["name"]}</div>'
        output += f'<p class="card__text"><br/>\n'
        output += f"<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n"
        output += f"<strong>Location:</strong> {animal["locations"][0]}<br/>\n"
        # add data of type value only if it exist in orig. data
        if "type" in animal["characteristics"]:
            output += f"<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n"
            output += "</p>"
            output += '</li><br/>\n'
        else:
            output += "</p>"
            output += '</li><br/>\n'
    return output


def main():
    input_animal = get_user_input()
    animals_data = load_data(input_animal)
    animals_string = generate_string(animals_data)
    html_template = read_html("animals_template.html")
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_string)
    write_html(new_html, ANIMAL_FILE)


if __name__ == "__main__":
    main()
