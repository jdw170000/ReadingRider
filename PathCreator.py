import json
import random
import os

def get_turn_amount():
    MAX_TURN = 0.5
    return random.uniform(-MAX_TURN, MAX_TURN)

def get_tile_width(word: str):
    return max(len(word), 4)

# pass the list of tokens from read_text
def create_track(text: str):
    tokens = [token for token in text.replace('\n', ' ').split(' ') if len(token) > 0]
    return [(token, get_turn_amount(), get_tile_width(token)) for token in tokens]

def menu():
    return int(input('''1. Create a new path! 2. Exit. (1,2): '''))

def save_track(filename: str, track: dict):
    current_path = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(f'{current_path}/paths/', exist_ok=True)
    with open(f'{current_path}/paths/{filename}.path', 'w') as f:
        json.dump(track, f)

def main():
    while(menu() < 2):
        track = dict()

        text = input('Enter the reading text: ')
        track['text'] = create_track(text)

        track['questions'] = list()
        question = input('Enter a question: ')
        while(question != ''):
            answer = input('Enter the answer: ')
            answers = list()
            while(answer != ''):
                answers.append(answer)
                answer = input('Enter a false answer choice (leave blank to move on): ')

            track['questions'].append((question, answers))

            question = input('Enter a question (leave blank to move on): ')
        
        batch_size = int(input('How many questions per test?: '))
        batch_size = min(batch_size, len(track['questions']))
        track['batch_size'] = batch_size

        track_name = input('Enter the track name: ')
        save_track(track_name, track)

if __name__ == '__main__':
    main()