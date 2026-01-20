import firebase_admin
from firebase_admin import credentials, firestore

# 1. Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. Define the questions data
# Structure: [Question Text, [Option A, B, C, D], Correct Answer, Difficulty]
questions_to_add = [
    # --- EASY (3 needed) ---
    ["Which country has the largest population in the world as of 2024?", ["China", "India", "USA", "Indonesia"], "India", "easy"],
    ["What is the capital city of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], "Canberra", "easy"], 
    ["Which international organization uses the 'Blue Helmet' for its peacekeeping forces?", ["NATO", "The Red Cross", "United Nations", "European Union"], "United Nations", "easy"], 
    ["Who was the first female Prime Minister of the United Kingdom?", ["Theresa May", "Angela Merkel", "Margaret Thatcher", "Indira Gandhi"], "Margaret Thatcher", "easy"], 
    ["What is the official currency of Japan?", ["Yuan", "Won", "Yen", "Ringgit"], "Yen", "easy"], 
    ["Which document serves as the supreme law of the United States?", ["The Declaration of Independence", "The Bill of Rights", "The Constitution", "The Federalist Papers"], "The Constitution", "easy"],
    ["Which country is known as the 'Land of the Rising Sun'?", ["China", "Japan", "South Korea", "Thailand"], "Japan", "easy"], 
    ["The Pyramids of Giza are located in which country?", ["Iraq", "Jordan", "Egypt", "Sudan"], "Egypt", "easy"], 
    ["Which US President was known as 'The Great Communicator'?", ["John F. Kennedy", "Ronald Reagan", "Bill Clinton", "Barack Obama"], "Ronald Reagan", "easy"], 
    ["What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "Pacific Ocean", "easy"], 
    ["Which country does NOT share a border with Brazil?", ["Argentina", "Chile", "Peru", "Colombia"], "Chile", "easy"], 
    ["The 'Statue of Liberty' was a gift to the USA from which country?", ["United Kingdom", "France", "Germany", "Italy"], "France", "easy"], 
    ["Who is the current President of France (as of 2024)?", ["François Hollande", "Nicolas Sarkozy", "Emmanuel Macron", "Marine Le Pen"], "Emmanuel Macron", "easy"], 
    ["Which city is the headquarters of the European Union?", ["Paris", "Geneva", "Brussels", "Berlin"], "Brussels", "easy"], 
    ["What is the primary language spoken in Brazil?", ["Spanish", "Portuguese", "French", "English"], "Portuguese", "easy"], 
    ["Which country is the world's largest producer of oil?", ["Russia", "Saudi Arabia", "USA", "Iraq"], "USA", "easy"], 
    ["Who wrote the 'Communist Manifesto'?", ["Vladimir Lenin", "Karl Marx & Friedrich Engels", "Joseph Stalin", "Leon Trotsky"], "Karl Marx & Friedrich Engels", "easy"], 
    ["Which African nation was formerly known as Abyssinia?", ["Nigeria", "Ethiopia", "Ghana", "Zimbabwe"], "Ethiopia", "easy"], 
    ["The 'Magna Carta' was signed in which country?", ["France", "England", "Italy", "Spain"], "England", "easy"], 
    ["How many members are in the US Senate?", ["50", "100", "435", "538"], "100", "easy"], 
    ["Which country is both an island and a continent?", ["Greenland", "Madagascar", "Australia", "Antarctica"], "Australia", "easy"], 
    ["What is the smallest country in the world by land area?", ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "Vatican City", "easy"], 
    ["Which organization is responsible for regulating global trade?", ["IMF", "World Bank", "WTO", "WHO"], "WTO", "easy"], 
    ["Who was the leader of the Soviet Union during World War II?", ["Nikita Khrushchev", "Mikhail Gorbachev", "Joseph Stalin", "Vladimir Lenin"], "Joseph Stalin", "easy"], 
    ["What color is the 'G' in the Google logo?", ["Red", "Yellow", "Blue", "Green"], "Blue", "easy"], 
    ["Which country hosted the 2022 FIFA World Cup?", ["Brazil", "Qatar", "Russia", "France"], "Qatar", "easy"], 
    ["What is the capital of Germany?", ["Munich", "Frankfurt", "Berlin", "Hamburg"], "Berlin", "easy"], 
    ["Which amendment to the US Constitution granted women the right to vote?", ["15th", "18th", "19th", "21st"], "19th", "easy"], 
    ["What is the most widely spoken language in the world (including non-native speakers)?", ["Mandarin Chinese", "Spanish", "English", "Hindi"], "English", "easy"], 
    ["The 'Apartheid' system was a policy of racial segregation in which country?", ["USA", "Zimbabwe", "South Africa", "Namibia"], "South Africa", "easy"], 
    ["Which river is the longest in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile", "easy"], 
    ["Who is the 'Father of the Indian Nation'?", ["Jawaharlal Nehru", "B.R. Ambedkar", "Mahatma Gandhi", "Sardar Patel"], "Mahatma Gandhi", "easy"], 
    ["Which planet is closest to the Sun?", ["Venus", "Earth", "Mars", "Mercury"], "Mercury", "easy"], 
    ["What is the legislative body of the United Kingdom called?", ["Congress", "Parliament", "Diet", "Duma"], "Parliament", "easy"], 
    ["Which country is famous for the 'Maple Leaf' on its flag?", ["USA", "Canada", "Switzerland", "Sweden"], "Canada", "easy"], 
    ["In which city is the Taj Mahal located?", ["Delhi", "Mumbai", "Agra", "Jaipur"], "Agra", "easy"], 
    ["What is the capital of Canada?", ["Toronto", "Montreal", "Ottawa", "Vancouver"], "Ottawa", "easy"], 
    ["Which country has the most volcanoes?", ["Japan", "Iceland", "Indonesia", "Italy"], "Indonesia", "easy"], 
    ["Who was the first person to walk on the moon?", ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], "Neil Armstrong", "easy"], 
    ["What is the national bird of the United States?", ["Golden Eagle", "Bald Eagle", "Peregrine Falcon", "Red-tailed Hawk"], "Bald Eagle", "easy"], 
    ["Which European country is shaped like a boot?", ["Greece", "Spain", "Italy", "Portugal"], "Italy", "easy"], 
    ["How many stars are on the flag of China?", ["3", "4", "5", "6"], "5", "easy"], 
    ["Which country is the world's largest democracy?", ["USA", "India", "Brazil", "Indonesia"], "India", "easy"], 
    ["What is the main ingredient in hummus?", ["Lentils", "Chickpeas", "Fava beans", "Soybeans"], "Chickpeas", "easy"], 
    ["Which US state is the largest by land area?", ["Texas", "California", "Alaska", "Montana"], "Alaska", "easy"], 
    ["What is the currency of the United Kingdom?", ["Euro", "Pound Sterling", "Dollar", "Franc"], "Pound Sterling", "easy"], 
    ["Which country is the home of the Nobel Prize?", ["Norway", "Sweden", "Switzerland", "Denmark"], "Sweden", "easy"], 
    ["What is the capital of Russia?", ["St. Petersburg", "Moscow", "Novosibirsk", "Kazan"], "Moscow", "easy"], 
    ["Which sea lies between Europe and Africa?", ["Red Sea", "Mediterranean Sea", "Caspian Sea", "Black Sea"], "Mediterranean Sea", "easy"], 
    ["Who is the current Prime Minister of India (as of 2024)?", ["Rahul Gandhi", "Narendra Modi", "Amit Shah", "Droupadi Murmu"], "Narendra Modi", "easy"],

    # --- MEDIUM (5 needed) ---
    ["Which element has the symbol 'Au'?", ["Silver", "Iron", "Gold", "Copper"], "Gold", "medium"],
    ["Who painted the Mona Lisa?", ["Van Gogh", "Da Vinci", "Picasso", "Monet"], "Da Vinci", "medium"],
    ["Which country is home to the Kangaroo?", ["India", "Australia", "South Africa", "Brazil"], "Australia", "medium"],
    ["What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific", "medium"],
    ["In which year did World War II end?", ["1943", "1944", "1945", "1946"], "1945", "medium"],

    # --- HARD (7 needed) ---
    ["What is the rarest blood type?", ["O Negative", "B Positive", "AB Negative", "Rh-Null"], "Rh-Null", "hard"],
    ["Which city is located on two continents?", ["Istanbul", "Cairo", "Panama City", "Moscow"], "Istanbul", "hard"],
    ["What is the powerhouse of the cell?", ["Nucleus", "Ribosome", "Mitochondria", "Vacuole"], "Mitochondria", "hard"],
    ["Which king signed the Magna Carta?", ["King John", "Henry VIII", "Richard I", "Edward I"], "King John", "hard"],
    ["What is the speed of light approx?", ["199k km/s", "299k km/s", "399k km/s", "499k km/s"], "299k km/s", "hard"],
    ["Who discovered Penicillin?", ["Marie Curie", "Alexander Fleming", "Newton", "Einstein"], "Alexander Fleming", "hard"],
    ["What is the smallest unit of memory?", ["Byte", "Bit", "Nibble", "Kilobyte"], "Bit", "hard"],
]

def upload():
    print("Starting upload...")
    for q in questions_to_add:
        data = {
            "text": q[0],
            "options": q[1],
            "answer": q[2],
            "difficulty": q[3]
        }
        # This adds the data to a collection named 'questions'
        db.collection("questions").add(data)
        print(f"Added: {q[0]}")
    print("--- Done! Your database is ready. ---")

if __name__ == "__main__":
    upload()