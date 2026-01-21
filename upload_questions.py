import firebase_admin
from firebase_admin import credentials, firestore
import hashlib

# 1. Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

questions_to_add = [
    # --- EASY QUESTIONS (1-50) ---
    {"text": "Which country has the largest population in the world as of 2024?", "options": ["China", "India", "USA", "Indonesia"], "answer": "India", "difficulty": "easy"},
    {"text": "What is the capital city of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": "Canberra", "difficulty": "easy"},
    {"text": "Which international organization uses the 'Blue Helmet'?", "options": ["NATO", "The Red Cross", "United Nations", "European Union"], "answer": "United Nations", "difficulty": "easy"},
    {"text": "Who was the first female PM of the UK?", "options": ["Theresa May", "Angela Merkel", "Margaret Thatcher", "Indira Gandhi"], "answer": "Margaret Thatcher", "difficulty": "easy"},
    {"text": "What is the official currency of Japan?", "options": ["Yuan", "Won", "Yen", "Ringgit"], "answer": "Yen", "difficulty": "easy"},
    {"text": "Which document is the supreme law of the US?", "options": ["Declaration of Independence", "Bill of Rights", "The Constitution", "Federalist Papers"], "answer": "The Constitution", "difficulty": "easy"},
    {"text": "Which country is known as the 'Land of the Rising Sun'?", "options": ["China", "Japan", "South Korea", "Thailand"], "answer": "Japan", "difficulty": "easy"},
    {"text": "The Pyramids of Giza are located in which country?", "options": ["Iraq", "Jordan", "Egypt", "Sudan"], "answer": "Egypt", "difficulty": "easy"},
    {"text": "Which US President was 'The Great Communicator'?", "options": ["John F. Kennedy", "Ronald Reagan", "Bill Clinton", "Barack Obama"], "answer": "Ronald Reagan", "difficulty": "easy"},
    {"text": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific", "difficulty": "easy"},
    {"text": "Which country does NOT share a border with Brazil?", "options": ["Argentina", "Chile", "Peru", "Colombia"], "answer": "Chile", "difficulty": "easy"},
    {"text": "The Statue of Liberty was a gift from which country?", "options": ["United Kingdom", "France", "Germany", "Italy"], "answer": "France", "difficulty": "easy"},
    {"text": "Who is the current President of France (2024)?", "options": ["François Hollande", "Nicolas Sarkozy", "Emmanuel Macron", "Marine Le Pen"], "answer": "Emmanuel Macron", "difficulty": "easy"},
    {"text": "Which city is the headquarters of the EU?", "options": ["Paris", "Geneva", "Brussels", "Berlin"], "answer": "Brussels", "difficulty": "easy"},
    {"text": "What is the primary language spoken in Brazil?", "options": ["Spanish", "Portuguese", "French", "English"], "answer": "Portuguese", "difficulty": "easy"},
    {"text": "Which country is the world's largest producer of oil?", "options": ["Russia", "Saudi Arabia", "USA", "Iraq"], "answer": "USA", "difficulty": "easy"},
    {"text": "Who wrote the 'Communist Manifesto'?", "options": ["Vladimir Lenin", "Karl Marx & Friedrich Engels", "Joseph Stalin", "Leon Trotsky"], "answer": "Karl Marx & Friedrich Engels", "difficulty": "easy"},
    {"text": "Which African nation was formerly Abyssinia?", "options": ["Nigeria", "Ethiopia", "Ghana", "Zimbabwe"], "answer": "Ethiopia", "difficulty": "easy"},
    {"text": "The 'Magna Carta' was signed in which country?", "options": ["France", "England", "Italy", "Spain"], "answer": "England", "difficulty": "easy"},
    {"text": "How many members are in the US Senate?", "options": ["50", "100", "435", "538"], "answer": "100", "difficulty": "easy"},
    {"text": "Which country is both an island and a continent?", "options": ["Greenland", "Madagascar", "Australia", "Antarctica"], "answer": "Australia", "difficulty": "easy"},
    {"text": "What is the smallest country in the world?", "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "answer": "Vatican City", "difficulty": "easy"},
    {"text": "Which organization regulates global trade?", "options": ["IMF", "World Bank", "WTO", "WHO"], "answer": "WTO", "difficulty": "easy"},
    {"text": "Who led the Soviet Union during WWII?", "options": ["Nikita Khrushchev", "Mikhail Gorbachev", "Joseph Stalin", "Vladimir Lenin"], "answer": "Joseph Stalin", "difficulty": "easy"},
    {"text": "What color is the 'G' in the Google logo?", "options": ["Red", "Yellow", "Blue", "Green"], "answer": "Blue", "difficulty": "easy"},
    {"text": "Which country hosted the 2022 FIFA World Cup?", "options": ["Brazil", "Qatar", "Russia", "France"], "answer": "Qatar", "difficulty": "easy"},
    {"text": "What is the capital of Germany?", "options": ["Munich", "Frankfurt", "Berlin", "Hamburg"], "answer": "Berlin", "difficulty": "easy"},
    {"text": "Which US amendment granted women the right to vote?", "options": ["15th", "18th", "19th", "21st"], "answer": "19th", "difficulty": "easy"},
    {"text": "Most widely spoken language (native + non-native)?", "options": ["Mandarin", "Spanish", "English", "Hindi"], "answer": "English", "difficulty": "easy"},
    {"text": "Apartheid was a policy in which country?", "options": ["USA", "Zimbabwe", "South Africa", "Namibia"], "answer": "South Africa", "difficulty": "easy"},
    {"text": "Which river is the longest in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile", "difficulty": "easy"},
    {"text": "Who is the 'Father of the Indian Nation'?", "options": ["J. Nehru", "B.R. Ambedkar", "Mahatma Gandhi", "S. Patel"], "answer": "Mahatma Gandhi", "difficulty": "easy"},
    {"text": "Which planet is closest to the Sun?", "options": ["Venus", "Earth", "Mars", "Mercury"], "answer": "Mercury", "difficulty": "easy"},
    {"text": "Legislative body of the UK?", "options": ["Congress", "Parliament", "Diet", "Duma"], "answer": "Parliament", "difficulty": "easy"},
    {"text": "Which country has the 'Maple Leaf' on its flag?", "options": ["USA", "Canada", "Switzerland", "Sweden"], "answer": "Canada", "difficulty": "easy"},
    {"text": "In which city is the Taj Mahal located?", "options": ["Delhi", "Mumbai", "Agra", "Jaipur"], "answer": "Agra", "difficulty": "easy"},
    {"text": "What is the capital of Canada?", "options": ["Toronto", "Montreal", "Ottawa", "Vancouver"], "answer": "Ottawa", "difficulty": "easy"},
    {"text": "Which country has the most volcanoes?", "options": ["Japan", "Iceland", "Indonesia", "Italy"], "answer": "Indonesia", "difficulty": "easy"},
    {"text": "First person to walk on the moon?", "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], "answer": "Neil Armstrong", "difficulty": "easy"},
    {"text": "National bird of the United States?", "options": ["Golden Eagle", "Bald Eagle", "Peregrine Falcon", "Hawk"], "answer": "Bald Eagle", "difficulty": "easy"},
    {"text": "Which European country is shaped like a boot?", "options": ["Greece", "Spain", "Italy", "Portugal"], "answer": "Italy", "difficulty": "easy"},
    {"text": "How many stars are on the flag of China?", "options": ["3", "4", "5", "6"], "answer": "5", "difficulty": "easy"},
    {"text": "Which country is the world's largest democracy?", "options": ["USA", "India", "Brazil", "Indonesia"], "answer": "India", "difficulty": "easy"},
    {"text": "What is the main ingredient in hummus?", "options": ["Lentils", "Chickpeas", "Fava beans", "Soybeans"], "answer": "Chickpeas", "difficulty": "easy"},
    {"text": "Which US state is the largest by land area?", "options": ["Texas", "California", "Alaska", "Montana"], "answer": "Alaska", "difficulty": "easy"},
    {"text": "What is the currency of the UK?", "options": ["Euro", "Pound Sterling", "Dollar", "Franc"], "answer": "Pound Sterling", "difficulty": "easy"},
    {"text": "Which country is the home of the Nobel Prize?", "options": ["Norway", "Sweden", "Switzerland", "Denmark"], "answer": "Sweden", "difficulty": "easy"},
    {"text": "What is the capital of Russia?", "options": ["St. Petersburg", "Moscow", "Novosibirsk", "Kazan"], "answer": "Moscow", "difficulty": "easy"},
    {"text": "Which sea lies between Europe and Africa?", "options": ["Red Sea", "Mediterranean Sea", "Caspian Sea", "Black Sea"], "answer": "Mediterranean Sea", "difficulty": "easy"},
    {"text": "Who is the current Prime Minister of India (2024)?", "options": ["Rahul Gandhi", "Narendra Modi", "Amit Shah", "D. Murmu"], "answer": "Narendra Modi", "difficulty": "easy"},

    # --- MEDIUM QUESTIONS ---
    {"text": "Geopolitical term 'soft power' refers to:", "options": ["Military strength", "Economic sanctions", "Cultural influence", "Nuclear deterrence"], "answer": "Cultural influence", "difficulty": "medium"},
    {"text": "Largest contributor to the UN budget?", "options": ["China", "Germany", "USA", "Japan"], "answer": "USA", "difficulty": "medium"},
    {"text": "The 'Zionist Movement' established a homeland for:", "options": ["Kurds", "Jewish people", "Palestinians", "Armenians"], "answer": "Jewish people", "difficulty": "medium"},
    {"text": "Name of the Turkish legislative body?", "options": ["The Grand National Assembly", "The Mejlis", "The Shura Council", "The Folketing"], "answer": "The Grand National Assembly", "difficulty": "medium"},
    {"text": "The 'Good Friday Agreement' ended conflict in:", "options": ["Balkans", "Northern Ireland", "Kashmir", "Basque Country"], "answer": "Northern Ireland", "difficulty": "medium"},
    {"text": "Buffer state between Russia and China?", "options": ["Kazakhstan", "Mongolia", "Kyrgyzstan", "Vietnam"], "answer": "Mongolia", "difficulty": "medium"},
    {"text": "Treaty of Westphalia (1648) created the concept of:", "options": ["Democracy", "Human Rights", "State Sovereignty", "Capitalism"], "answer": "State Sovereignty", "difficulty": "medium"},
    {"text": "Nation with the most UNESCO World Heritage Sites?", "options": ["China", "Italy", "France", "Spain"], "answer": "Italy", "difficulty": "medium"},
    {"text": "What is the 'Gherkin' in London?", "options": ["Museum", "Royal park", "Skyscraper", "Bridge"], "answer": "Skyscraper", "difficulty": "medium"},
    {"text": "GCC headquarters is in which city?", "options": ["Dubai", "Riyadh", "Abu Dhabi", "Doha"], "answer": "Riyadh", "difficulty": "medium"},
    {"text": "Which country has a non-rectangular flag?", "options": ["Bhutan", "Nepal", "Switzerland", "Vatican City"], "answer": "Nepal", "difficulty": "medium"},
    {"text": "Who coined the term 'Iron Curtain'?", "options": ["Harry Truman", "Winston Churchill", "F.D.R.", "Dwight Eisenhower"], "answer": "Winston Churchill", "difficulty": "medium"},
    {"text": "Largest country in South America by area?", "options": ["Argentina", "Brazil", "Colombia", "Peru"], "answer": "Brazil", "difficulty": "medium"},
    {"text": "Kuril Islands dispute involves which two countries?", "options": ["China/Japan", "Russia/Japan", "North/South Korea", "Philippines/China"], "answer": "Russia/Japan", "difficulty": "medium"},
    {"text": "Primary function of the ICJ?", "options": ["Try individuals", "Settle legal disputes between states", "Manage trade", "Monitor elections"], "answer": "Settle legal disputes between states", "difficulty": "medium"},
    {"text": "World's largest producer of cocoa?", "options": ["Ghana", "Ivory Coast", "Brazil", "Indonesia"], "answer": "Ivory Coast", "difficulty": "medium"},
    {"text": "Camp David Accords (1978) were between:", "options": ["Israel/Jordan", "Israel/Egypt", "USA/USSR", "Iraq/Iran"], "answer": "Israel/Egypt", "difficulty": "medium"},
    {"text": "Capital of Kazakhstan (renamed in 2022)?", "options": ["Almaty", "Astana", "Nur-Sultan", "Tashkent"], "answer": "Astana", "difficulty": "medium"},
    {"text": "Agreement to limit warming to below 2 degrees?", "options": ["Kyoto Protocol", "Paris Agreement", "Montreal Protocol", "Geneva Convention"], "answer": "Paris Agreement", "difficulty": "medium"},
    {"text": "Chagos Islands dispute involves:", "options": ["UK/Mauritius", "France/Comoros", "USA/Cuba", "India/Sri Lanka"], "answer": "UK/Mauritius", "difficulty": "medium"},
    {"text": "World's largest proven coal reserves?", "options": ["China", "Russia", "USA", "Australia"], "answer": "USA", "difficulty": "medium"},
    {"text": "What is the 'Schengen Area'?", "options": ["Military alliance", "Zone with abolished internal borders", "Trade agreement", "Space program"], "answer": "Zone with abolished internal borders", "difficulty": "medium"},
    {"text": "The 'Pink Tide' refers to a political trend in:", "options": ["Southeast Asia", "Latin America", "Eastern Europe", "North Africa"], "answer": "Latin America", "difficulty": "medium"},
    {"text": "Which sea is shrinking due to Soviet irrigation?", "options": ["Caspian Sea", "Aral Sea", "Dead Sea", "Black Sea"], "answer": "Aral Sea", "difficulty": "medium"},
    {"text": "What is the legislative body of Russia?", "options": ["The Duma", "The Bundestag", "The Diet", "The Cortes"], "answer": "The Duma", "difficulty": "medium"},
    {"text": "Who is the 'Grand Ayatollah' of Iran?", "options": ["Ebrahim Raisi", "Ali Khamenei", "Hassan Rouhani", "M. Ahmadinejad"], "answer": "Ali Khamenei", "difficulty": "medium"},
    {"text": "Benelux union includes Belgium, Netherlands and:", "options": ["Switzerland", "Luxembourg", "Liechtenstein", "Denmark"], "answer": "Luxembourg", "difficulty": "medium"},
    {"text": "Hosted first modern Olympic Games in 1896?", "options": ["Paris", "Athens", "Rome", "London"], "answer": "Athens", "difficulty": "medium"},
    {"text": "Boundary line between North and South Korea?", "options": ["38th Parallel", "49th Parallel", "Radcliffe Line", "Durand Line"], "answer": "38th Parallel", "difficulty": "medium"},
    {"text": "OPEC+ group includes major non-member:", "options": ["USA", "Russia", "China", "Norway"], "answer": "Russia", "difficulty": "medium"},
    {"text": "Which country is known as the 'Hexagon'?", "options": ["Spain", "France", "Poland", "Germany"], "answer": "France", "difficulty": "medium"},
    {"text": "First President of the Russian Federation?", "options": ["M. Gorbachev", "Boris Yeltsin", "Vladimir Putin", "D. Medvedev"], "answer": "Boris Yeltsin", "difficulty": "medium"},
    {"text": "Silk Road historically connected China with:", "options": ["Americas", "Europe/Mediterranean", "Sub-Saharan Africa", "Australia"], "answer": "Europe/Mediterranean", "difficulty": "medium"},
    {"text": "Largest desert in the world?", "options": ["Sahara", "Gobi", "Antarctica", "Arabian"], "answer": "Antarctica", "difficulty": "medium"},
    {"text": "World's top producer of lithium?", "options": ["Chile", "Australia", "China", "Argentina"], "answer": "Australia", "difficulty": "medium"},
    {"text": "Balfour Declaration (1917) supported a home for:", "options": ["Arabs", "Jews", "Armenians", "Kurds"], "answer": "Jews", "difficulty": "medium"},
    {"text": "Which US state was once an independent republic?", "options": ["Florida", "Texas", "Ohio", "Nevada"], "answer": "Texas", "difficulty": "medium"},
    {"text": "Official residence of the President of India?", "options": ["White House", "Rashtrapati Bhavan", "10 Downing Street", "Kremlin"], "answer": "Rashtrapati Bhavan", "difficulty": "medium"},
    {"text": "Home to the world's tallest building (Burj Khalifa)?", "options": ["Saudi Arabia", "UAE", "Qatar", "China"], "answer": "UAE", "difficulty": "medium"},
    {"text": "Nuremberg Trials prosecuted leaders of which regime?", "options": ["Soviet Union", "Nazi Germany", "Fascist Italy", "Imperial Japan"], "answer": "Nazi Germany", "difficulty": "medium"},
    {"text": "Currency used by majority of EU nations?", "options": ["Franc", "Euro", "Mark", "Pound"], "answer": "Euro", "difficulty": "medium"},
    {"text": "World's leading producer of coffee?", "options": ["Vietnam", "Colombia", "Brazil", "Ethiopia"], "answer": "Brazil", "difficulty": "medium"},
    {"text": "Maginot Line was a barrier built by which country?", "options": ["Germany", "France", "Poland", "Belgium"], "answer": "France", "difficulty": "medium"},
    {"text": "Strait separates the UK from France?", "options": ["Gibraltar", "Dover", "Hormuz", "Bosphorus"], "answer": "Dover", "difficulty": "medium"},
    {"text": "Primary author of US Declaration of Independence?", "options": ["Washington", "Jefferson", "Franklin", "Adams"], "answer": "Jefferson", "difficulty": "medium"},
    {"text": "World's largest producer of silver?", "options": ["Peru", "China", "Mexico", "USA"], "answer": "Mexico", "difficulty": "medium"},
    {"text": "Most populous city in Africa?", "options": ["Cairo", "Lagos", "Kinshasa", "Nairobi"], "answer": "Lagos", "difficulty": "medium"},
    {"text": "Lowest point on Earth's surface?", "options": ["Caspian Sea", "Dead Sea", "Aral Sea", "Lake Baikal"], "answer": "Dead Sea", "difficulty": "medium"},
    {"text": "Prague Spring occurred in which year?", "options": ["1956", "1968", "1989", "1972"], "answer": "1968", "difficulty": "medium"},
    {"text": "Longest coastline in the world?", "options": ["Russia", "USA", "Canada", "Australia"], "answer": "Canada", "difficulty": "medium"},

    # --- HARD QUESTIONS ---
    {"text": "Thucydides Trap describes war when:", "options": ["Rising power threatens hegemon", "Power tries regain territory", "Minor powers fight resources", "Civil war occurs"], "answer": "Rising power threatens hegemon", "difficulty": "hard"},
    {"text": "Treaty divided 'New World' (Spain/Portugal)?", "options": ["Versailles", "Tordesillas", "Utrecht", "Westphalia"], "answer": "Tordesillas", "difficulty": "hard"},
    {"text": "Suwalki Gap is between which two entities?", "options": ["Russia/Belarus", "Poland/Lithuania", "Estonia/Latvia", "Ukraine/Moldova"], "answer": "Poland/Lithuania", "difficulty": "hard"},
    {"text": "Author of 'The Clash of Civilizations'?", "options": ["Fukuyama", "Huntington", "Kissinger", "Brzezinski"], "answer": "Huntington", "difficulty": "hard"},
    {"text": "Nine-Dash Line is claimed by China in:", "options": ["East China Sea", "South China Sea", "Yellow Sea", "Sea of Japan"], "answer": "South China Sea", "difficulty": "hard"},
    {"text": "Game Theory: one person's gain = another's loss?", "options": ["Win-Win", "Zero-Sum", "Stalemate", "Prisoner's Dilemma"], "answer": "Zero-Sum", "difficulty": "hard"},
    {"text": "African borders decided at which 1884 Conference?", "options": ["Vienna", "Berlin", "Paris", "London"], "answer": "Berlin", "difficulty": "hard"},
    {"text": "Montreux Convention (1936) regulates passage through:", "options": ["Malacca/Sunda", "Bosphorus/Dardanelles", "Hormuz/Bab el-Mandeb", "Gibraltar/Messina"], "answer": "Bosphorus/Dardanelles", "difficulty": "hard"},
    {"text": "Rule of a small group for selfish purposes?", "options": ["Autocracy", "Oligarchy", "Plutocracy", "Meritocracy"], "answer": "Oligarchy", "difficulty": "hard"},
    {"text": "Holodomor man-made famine occurred in:", "options": ["Kazakhstan", "Ukraine", "Belarus", "Georgia"], "answer": "Ukraine", "difficulty": "hard"},
    {"text": "What is 'The Great Game'?", "options": ["Chess tournament", "Britain/Russia rivalry", "Scramble for Africa", "Space race"], "answer": "Britain/Russia rivalry", "difficulty": "hard"},
    {"text": "Who authored 'The Wealth of Nations' (1776)?", "options": ["Keynes", "Adam Smith", "Ricardo", "Marx"], "answer": "Adam Smith", "difficulty": "hard"},
    {"text": "Durand Line is border between which two countries?", "options": ["India/Pakistan", "Afghanistan/Pakistan", "Iran/Iraq", "China/India"], "answer": "Afghanistan/Pakistan", "difficulty": "hard"},
    {"text": "Architect of 'Realpolitik' in 19th-century Prussia?", "options": ["Napoleon III", "Bismarck", "Metternich", "Wilhelm II"], "answer": "Bismarck", "difficulty": "hard"},
    {"text": "McMahon Line is boundary dispute between:", "options": ["India/China", "India/Myanmar", "China/Vietnam", "Pakistan/China"], "answer": "India/China", "difficulty": "hard"},
    {"text": "Island divided by the 'Green Line'?", "options": ["Crete", "Cyprus", "Rhodes", "Malta"], "answer": "Cyprus", "difficulty": "hard"},
    {"text": "Heartland Theory was proposed by:", "options": ["Mahan", "Mackinder", "Spykman", "Haushofer"], "answer": "Mackinder", "difficulty": "hard"},
    {"text": "Only country with three official capital cities?", "options": ["Switzerland", "South Africa", "Bolivia", "Malaysia"], "answer": "South Africa", "difficulty": "hard"},
    {"text": "What does UNCLOS stand for?", "options": ["Convention on Law of Sea", "Council Liberal Societies", "Committee Land Science", "Maritime Trade Agreement"], "answer": "Convention on Law of Sea", "difficulty": "hard"},
    {"text": "Sykes-Picot Agreement (1916) divided which region?", "options": ["SE Asia", "Middle East", "West Africa", "South America"], "answer": "Middle East", "difficulty": "hard"},
    {"text": "Which country currently occupies Golan Heights?", "options": ["Syria", "Israel", "Lebanon", "Jordan"], "answer": "Israel", "difficulty": "hard"},
    {"text": "Bretton Woods led to creation of which two?", "options": ["UN/NATO", "IMF/World Bank", "WTO/WHO", "EU/ASEAN"], "answer": "IMF/World Bank", "difficulty": "hard"},
    {"text": "First Secretary-General of the United Nations?", "options": ["Hammarskjöld", "Trygve Lie", "U Thant", "Kofi Annan"], "answer": "Trygve Lie", "difficulty": "hard"},
    {"text": "Treaty of Shimonoseki ended first war between:", "options": ["Japan/Russia", "Japan/China", "China/UK", "USA/Spain"], "answer": "Japan/China", "difficulty": "hard"},
    {"text": "Democracies are hesitant to go to war with one another?", "options": ["Institutionalism", "Democratic Peace Theory", "Realism", "Constructivism"], "answer": "Democratic Peace Theory", "difficulty": "hard"},
    {"text": "Scramble for Africa formalised at:", "options": ["Vienna", "Berlin", "Paris", "Yalta"], "answer": "Berlin", "difficulty": "hard"},
    {"text": "Who wrote 'The Prince'?", "options": ["Hobbes", "Machiavelli", "Locke", "Rousseau"], "answer": "Machiavelli", "difficulty": "hard"},
    {"text": "What is the 'Resource Curse'?", "options": ["Resources = less growth", "Resources = disasters", "No resources = fastest growth", "Resources = inflation"], "answer": "Resources = less growth", "difficulty": "hard"},
    {"text": "Marshall Plan was to rebuild which region?", "options": ["East Asia", "Western Europe", "Latin America", "Eastern Europe"], "answer": "Western Europe", "difficulty": "hard"},
    {"text": "Country with the most time zones?", "options": ["Russia", "USA", "France", "China"], "answer": "France", "difficulty": "hard"},
    {"text": "Kaliningrad Oblast is an exclave of which country?", "options": ["Germany", "Poland", "Russia", "Lithuania"], "answer": "Russia", "difficulty": "hard"},
    {"text": "Strait of Malacca primarily known for:", "options": ["Deepest strait", "Major shipping lane", "Proximity Antarctica", "Pearl diving"], "answer": "Major shipping lane", "difficulty": "hard"},
    {"text": "Brezhnev Doctrine asserted USSR right to:", "options": ["Trade West", "Intervene socialist countries", "Build nuclear", "Open borders"], "answer": "Intervene socialist countries", "difficulty": "hard"},
    {"text": "Which country is 'Cradle of Liberty'?", "options": ["France", "USA", "Greece", "UK"], "answer": "USA", "difficulty": "hard"},
    {"text": "Falklands War: UK fought which country?", "options": ["Chile", "Argentina", "Brazil", "Spain"], "answer": "Argentina", "difficulty": "hard"},
    {"text": "Author of 'Princeps of International Law'?", "options": ["Grotius", "Bodin", "Aquinas", "Kant"], "answer": "Grotius", "difficulty": "hard"},
    {"text": "World's largest landlocked nation?", "options": ["Mongolia", "Kazakhstan", "Bolivia", "Chad"], "answer": "Kazakhstan", "difficulty": "hard"},
    {"text": "Shatt al-Arab waterway caused war between:", "options": ["Iraq/Iran", "Saudi/Yemen", "Egypt/Sudan", "Syria/Turkey"], "answer": "Iraq/Iran", "difficulty": "hard"},
    {"text": "Treaty established the European Union in 1993?", "options": ["Rome", "Maastricht", "Lisbon", "Versailles"], "answer": "Maastricht", "difficulty": "hard"},
    {"text": "African Union is headquartered in:", "options": ["Johannesburg", "Addis Ababa", "Nairobi", "Lagos"], "answer": "Addis Ababa", "difficulty": "hard"},
    {"text": "Peloponnesian War primary source?", "options": ["Herodotus", "Thucydides", "Plato", "Aristotle"], "answer": "Thucydides", "difficulty": "hard"},
    {"text": "Treaty of Portsmouth (1905) ended war between:", "options": ["Russia/Germany", "Russia/Japan", "Russia/Turkey", "USA/UK"], "answer": "Russia/Japan", "difficulty": "hard"},
    {"text": "Highest GDP per capita (nominal) currently?", "options": ["USA", "Luxembourg", "Qatar", "Switzerland"], "answer": "Luxembourg", "difficulty": "hard"},
    {"text": "Orange Revolution took place in:", "options": ["Georgia", "Ukraine", "Kyrgyzstan", "Belarus"], "answer": "Ukraine", "difficulty": "hard"},
    {"text": "Exclusive Economic Zone distance from coast?", "options": ["12nm", "200nm", "500nm", "100nm"], "answer": "200nm", "difficulty": "hard"},
    {"text": "US President issued 'Fourteen Points'?", "options": ["Roosevelt", "Wilson", "Taft", "Lincoln"], "answer": "Wilson", "difficulty": "hard"},
    {"text": "Good Neighbor Policy was toward which region?", "options": ["Europe", "Latin America", "East Asia", "Middle East"], "answer": "Latin America", "difficulty": "hard"},
    {"text": "Only country to use nuclear weapons in combat?", "options": ["Russia", "USA", "UK", "France"], "answer": "USA", "difficulty": "hard"},
    {"text": "Magna Carta issued during which King's reign?", "options": ["Richard", "John", "Henry VIII", "Edward I"], "answer": "John", "difficulty": "hard"},
    {"text": "Ideology: classless, stateless society?", "options": ["Fascism", "Communism", "Liberalism", "Socialism"], "answer": "Communism", "difficulty": "hard"},
    


{"text": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars", "difficulty": "easy"},
{"text": "What is the name of the galaxy that contains our Solar System?", "options": ["Andromeda", "Sombrero", "The Milky Way", "Triangulum"], "answer": "The Milky Way", "difficulty": "easy"},
{"text": "In Greek mythology, who is the King of the Gods and ruler of Mount Olympus?", "options": ["Poseidon", "Hades", "Zeus", "Apollo"], "answer": "Zeus", "difficulty": "easy"},
{"text": "Which Norse god is famous for wielding the hammer Mjölnir?", "options": ["Odin", "Loki", "Thor", "Balder"], "answer": "Thor", "difficulty": "easy"},
{"text": "How many World Drivers' Championship titles has Lewis Hamilton won (as of 2024)?", "options": ["5", "7", "9", "6"], "answer": "7", "difficulty": "easy"},
{"text": "Which iconic Italian team uses a Prancing Horse as its logo?", "options": ["McLaren", "Red Bull", "Ferrari", "Mercedes"], "answer": "Ferrari", "difficulty": "easy"},
{"text": "On which surface is the Wimbledon championship played?", "options": ["Clay", "Hard Court", "Grass", "Carpet"], "answer": "Grass", "difficulty": "easy"},
{"text": "How many points is a standard free throw worth in basketball?", "options": ["1", "2", "3", "0"], "answer": "1", "difficulty": "easy"},
{"text": "Which team does Stephen Curry play for?", "options": ["LA Lakers", "Golden State Warriors", "Chicago Bulls", "Miami Heat"], "answer": "Golden State Warriors", "difficulty": "easy"},
{"text": "Who is often referred to as the King of Pop?", "options": ["Elvis Presley", "Prince", "Michael Jackson", "Freddie Mercury"], "answer": "Michael Jackson", "difficulty": "easy"},
{"text": "Which musical instrument has 88 keys?", "options": ["Guitar", "Harp", "Piano", "Accordion"], "answer": "Piano", "difficulty": "easy"},
{"text": "What is the largest continent on Earth by land area?", "options": ["Africa", "North America", "Asia", "Antarctica"], "answer": "Asia", "difficulty": "easy"},
{"text": "Which river is the longest in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile", "difficulty": "easy"},
{"text": "Who wrote the 'Harry Potter' series?", "options": ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"], "answer": "J.K. Rowling", "difficulty": "easy"},
{"text": "In which year did the United States declare its independence?", "options": ["1492", "1776", "1812", "1945"], "answer": "1776", "difficulty": "easy"},
{"text": "Who was the first President of the United States?", "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"], "answer": "George Washington", "difficulty": "easy"},
{"text": "Which fruit is traditionally used to make cider?", "options": ["Pear", "Apple", "Grape", "Orange"], "answer": "Apple", "difficulty": "easy"},
{"text": "How many colors are in a rainbow?", "options": ["5", "6", "7", "8"], "answer": "7", "difficulty": "easy"},
{"text": "What was the name of the unsinkable ship that sank in 1912?", "options": ["Lusitania", "Titanic", "Britannica", "Queen Mary"], "answer": "Titanic", "difficulty": "easy"},
{"text": "What type of natural disaster involves a giant sea wave caused by an underwater earthquake?", "options": ["Hurricane", "Tornado", "Tsunami", "Blizzard"], "answer": "Tsunami", "difficulty": "easy"},
{"text": "The Great Fire of 1666 devastated which major city?", "options": ["Paris", "Rome", "London", "New York"], "answer": "London", "difficulty": "easy"},
{"text": "Which planet is famous for its prominent, beautiful rings?", "options": ["Mars", "Jupiter", "Saturn", "Neptune"], "answer": "Saturn", "difficulty": "easy"},
{"text": "What do we call a person who travels into space?", "options": ["Astronomer", "Astronaut", "Astrologer", "Pilot"], "answer": "Astronaut", "difficulty": "easy"},
{"text": "In Greek mythology, what was the name of the king who turned everything he touched into gold?", "options": ["Minos", "Midas", "Agamemnon", "Priam"], "answer": "Midas", "difficulty": "easy"},
{"text": "Which Roman god was the ruler of the sea?", "options": ["Jupiter", "Mars", "Neptune", "Vulcan"], "answer": "Neptune", "difficulty": "easy"},
{"text": "What is the name for the area where cars stop for tire changes and repairs during a race?", "options": ["Paddock", "Garage", "Pit lane", "Grid"], "answer": "Pit lane", "difficulty": "easy"},
{"text": "How many wheels does a standard Formula 1 car have?", "options": ["3", "4", "6", "8"], "answer": "4", "difficulty": "easy"},
{"text": "What is the term for a serve that the receiver cannot even touch?", "options": ["Fault", "Let", "Ace", "Smash"], "answer": "Ace", "difficulty": "easy"},
{"text": "What is the height of a standard NBA basketball rim in feet?", "options": ["8 feet", "9 feet", "10 feet", "12 feet"], "answer": "10 feet", "difficulty": "easy"},
{"text": "Which team is famous for their green jerseys and playing in Boston?", "options": ["Nets", "Knicks", "Celtics", "Bulls"], "answer": "Celtics", "difficulty": "easy"},
{"text": "Which group sang the hits Dancing Queen and Mamma Mia?", "options": ["The Beatles", "ABBA", "Bee Gees", "Queen"], "answer": "ABBA", "difficulty": "easy"},
{"text": "What is the name of the stick a conductor uses to lead an orchestra?", "options": ["Wand", "Baton", "Staff", "Bow"], "answer": "Baton", "difficulty": "easy"},
{"text": "What is the capital city of France?", "options": ["Lyon", "Marseille", "Paris", "Nice"], "answer": "Paris", "difficulty": "easy"},
{"text": "Which country is both a country and a continent?", "options": ["Brazil", "Australia", "India", "Canada"], "answer": "Australia", "difficulty": "easy"},
{"text": "In 'The Jungle Book', what kind of animal is Baloo?", "options": ["Panther", "Tiger", "Bear", "Snake"], "answer": "Bear", "difficulty": "easy"},
{"text": "The Great Wall of China was primarily built to protect against which group?", "options": ["Vikings", "Romans", "Mongols", "Aztecs"], "answer": "Mongols", "difficulty": "easy"},
{"text": "Which planet has the shortest day in our solar system, rotating once every 10 hours?", "options": ["Saturn", "Neptune", "Jupiter", "Uranus"], "answer": "Jupiter", "difficulty": "medium"},
{"text": "What is the name of the largest moon of Saturn?", "options": ["Ganymede", "Titan", "Europa", "lo"], "answer": "Titan", "difficulty": "medium"},
{"text": "In which year did Neil Armstrong and Buzz Aldrin first walk on the moon?", "options": ["1963", "1969", "1972", "1967"], "answer": "1969", "difficulty": "medium"},
{"text": "In Egyptian mythology, who is the god of the afterlife, often depicted with green skin?", "options": ["Anubis", "Ra", "Osiris", "Set"], "answer": "Osiris", "difficulty": "medium"},
{"text": "Which hero of Greek myth performed twelve labors to atone for his crimes?", "options": ["Jason", "Heracles (Hercules)", "Perseus", "Bellerophon"], "answer": "Heracles (Hercules)", "difficulty": "medium"},
{"text": "What is the name of the three-headed dog that guards the entrance to the Underworld?", "options": ["Hydra", "Cerberus", "Chimera", "Minotaur"], "answer": "Cerberus", "difficulty": "medium"},
{"text": "In Roman mythology, Diana is the goddess of the hunt. Who is her Greek counterpart?", "options": ["Athena", "Artemis", "Aphrodite", "Hera"], "answer": "Artemis", "difficulty": "medium"},
{"text": "Which driver holds the record for the most race wins in Formula 1 history?", "options": ["Michael Schumacher", "Ayrton Senna", "Lewis Hamilton", "Sebastian Vettel"], "answer": "Lewis Hamilton", "difficulty": "medium"},
{"text": "The Eau Rouge corner is part of which famous F1 circuit?", "options": ["Silverstone", "Monza", "Spa-Francorganchamps", "Monaco"], "answer": "Spa-Francorganchamps", "difficulty": "medium"},
{"text": "Which team did Ayrton Senna drive for when he won his three world titles?", "options": ["Lotus", "Ferrari", "McLaren", "Williams"], "answer": "McLaren", "difficulty": "medium"},
{"text": "Who was the first ever Formula 1 World Champion in 1950?", "options": ["Juan Manuel Fangio", "Giuseppe Farina", "Alberto Ascari", "Stirling Moss"], "answer": "Giuseppe Farina", "difficulty": "medium"},
{"text": "Which female tennis player has won the most Grand Slam singles titles in the Open Era?", "options": ["Steffi Graf", "Margaret Court", "Serena Williams", "Martina Navratilova"], "answer": "Serena Williams", "difficulty": "medium"},
{"text": "What is the name of the stadium that hosts the final of the French Open?", "options": ["Rod Laver Arena", "Arthur Ashe Stadium", "Court Philippe-Chatrier", "Centre Court"], "answer": "Court Philippe-Chatrier", "difficulty": "medium"},
{"text": "The Rocket is the nickname of which legendary Australian tennis player?", "options": ["Björn Borg", "Rod Laver", "Ken Rosewall", "Patrick Rafter"], "answer": "Rod Laver", "difficulty": "medium"},
{"text": "Which country does the player Rafael Nadal represent?", "options": ["Argentina", "Italy", "Spain", "Portugal"], "answer": "Spain", "difficulty": "medium"},
{"text": "Which NBA player was famously known by the nickname The Answer?", "options": ["Shaquille O'Neal", "Allen Iverson", "Tim Duncan", "Kevin Garnett"], "answer": "Allen Iverson", "difficulty": "medium"},
{"text": "How many championships did Michael Jordan win with the Chicago Bulls?", "options": ["4", "5", "6", "7"], "answer": "6", "difficulty": "medium"},
{"text": "Who holds the record for the most assists in NBA history?", "options": ["Magic Johnson", "John Stockton", "Jason Kidd", "Chris Paul"], "answer": "John Stockton", "difficulty": "medium"},
{"text": "Which team won the very first NBA championship in 1947?", "options": ["Boston Celtics", "New York Knicks", "Philadelphia Warriors", "Minneapolis Lakers"], "answer": "Philadelphia Warriors", "difficulty": "medium"},
{"text": "Which band released the best-selling album 'The Dark Side of the Moon'?", "options": ["Led Zeppelin", "Pink Floyd", "The Who", "Fleetwood Mac"], "answer": "Pink Floyd", "difficulty": "medium"},
{"text": "Who wrote the famous Messiah oratorio, including the Hallelujah chorus?", "options": ["Bach", "Beethoven", "Handel", "Mozart"], "answer": "Handel", "difficulty": "medium"},
{"text": "Which female artist is known as the Queen of Soul?", "options": ["Whitney Houston", "Aretha Franklin", "Diana Ross", "Tina Turner"], "answer": "Aretha Franklin", "difficulty": "medium"},
{"text": "In which city was the legendary rock band The Beatles formed?", "options": ["London", "Manchester", "Liverpool", "Birmingham"], "answer": "Liverpool", "difficulty": "medium"},
{"text": "Which artist released the 2015 hit album '25'?", "options": ["Taylor Swift", "Adele", "Katy Perry", "Beyoncé"], "answer": "Adele", "difficulty": "medium"},
{"text": "Mount Kilimanjaro, the highest mountain in Africa, is located in which country?", "options": ["Kenya", "Ethiopia", "Tanzania", "Uganda"], "answer": "Tanzania", "difficulty": "medium"},
{"text": "What is the capital city of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": "Canberra", "difficulty": "medium"},
{"text": "Which sea separates the continents of Europe and Africa?", "options": ["Red Sea", "Mediterranean Sea", "Caspian Sea", "Black Sea"], "answer": "Mediterranean Sea", "difficulty": "medium"},
{"text": "In which country would you find the ancient city of Petra?", "options": ["Egypt", "Jordan", "Iraq", "Turkey"], "answer": "Jordan", "difficulty": "medium"},
{"text": "Which U.S. state is known as the Sunshine State?", "options": ["California", "Texas", "Florida", "Hawaii"], "answer": "Florida", "difficulty": "medium"},
{"text": "In 'The Great Gatsby', who is the narrator of the story?", "options": ["Jay Gatsby", "Tom Buchanan", "Nick Carraway", "Daisy Buchanan"], "answer": "Nick Carraway", "difficulty": "medium"},
{"text": "Which Russian author wrote 'War and Peace'?", "options": ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Vladimir Nabokov"], "answer": "Leo Tolstoy", "difficulty": "medium"},
{"text": "What is the name of the fictional land where 'The Hobbit' takes place?", "options": ["Westeros", "Narnia", "Middle-earth", "Neverland"], "answer": "Middle-earth", "difficulty": "medium"},
{"text": "Who wrote the 1818 novel 'Frankenstein'?", "options": ["Jane Austen", "Mary Shelley", "Charlotte Brontë", "Emily Brontë"], "answer": "Mary Shelley", "difficulty": "medium"},
{"text": "Which French military leader was defeated at the Battle of Waterloo in 1815?", "options": ["Louis XIV", "Charles de Gaulle", "Napoleon Bonaparte", "Maximilien Robespierre"], "answer": "Napoleon Bonaparte", "difficulty": "medium"},
{"text": "The Magna Carta was signed by King John of England in which year?", "options": ["1066", "1215", "1492", "1588"], "answer": "1215", "difficulty": "medium"},
{"text": "Which civilization built the ancient city of Machu Picchu?", "options": ["Aztec", "Mayan", "Incas", "Olmec"], "answer": "Incas", "difficulty": "medium"},
{"text": "Who was the primary author of the Declaration of Independence?", "options": ["Benjamin Franklin", "Thomas Jefferson", "James Madison", "Alexander Hamilton"], "answer": "Thomas Jefferson", "difficulty": "medium"},
{"text": "What is the chemical symbol for the element Gold?", "options": ["Ag", "Au", "Fe", "Pb"], "answer": "Au", "difficulty": "medium"},
{"text": "Which language has the most native speakers in the world?", "options": ["English", "Spanish", "Mandarin Chinese", "Hindi"], "answer": "Mandarin Chinese", "difficulty": "medium"},
{"text": "In chess, which piece can only move diagonally?", "options": ["Rook", "Knight", "Bishop", "Queen"], "answer": "Bishop", "difficulty": "medium"},
{"text": "What is the largest organ in the human body?", "options": ["Liver", "Brain", "Skin", "Lungs"], "answer": "Skin", "difficulty": "medium"},
{"text": "The eruption of Mount Vesuvius in 79 AD destroyed which two Roman cities?", "options": ["Rome and Naples", "Pompeii and Herculaneum", "Florence and Venice", "Milan and Genoa"], "answer": "Pompeii and Herculaneum", "difficulty": "medium"},
{"text": "The Dust Bowl was a period of severe dust storms that affected which region in the 1930s?", "options": ["Australian Outback", "Sahara Desert", "North American Prairies", "Gobi Desert"], "answer": "North American Prairies", "difficulty": "medium"},
{"text": "Which 2005 hurricane caused catastrophic damage to the city of New Orleans?", "options": ["Andrew", "Katrina", "Sandy", "Irma"], "answer": "Katrina", "difficulty": "medium"},
{"text": "What was the name of the toxic gas leak that occurred in Bhopal, India, in 1984?", "options": ["Methyl Isocyanate", "Carbon Monoxide", "Chlorine Gas", "Ammonia"], "answer": "Methyl Isocyanate", "difficulty": "medium"},
{"text": "The Great Famine of the 1840s, caused by potato blight, occurred in which country?", "options": ["Scotland", "Ireland", "Germany", "Poland"], "answer": "Ireland", "difficulty": "medium"},
{"text": "Which Japanese city was the first to be struck by an atomic bomb in 1945?", "options": ["Tokyo", "Kyoto", "Hiroshima", "Nagasaki"], "answer": "Hiroshima", "difficulty": "medium"},
{"text": "In 1906, a major earthquake and subsequent fires destroyed much of which US city?", "options": ["Los Angeles", "Seattle", "San Francisco", "Chicago"], "answer": "San Francisco", "difficulty": "medium"},
{"text": "What is the name of the path a planet takes around the sun?", "options": ["Axis", "Orbit", "Rotation", "Revolution"], "answer": "Orbit", "difficulty": "medium"},
{"text": "Which galaxy is on a collision course with the Milky Way?", "options": ["Andromeda", "Whirlpool", "Sombrero", "Pinwheel"], "answer": "Andromeda", "difficulty": "medium"},
{"text": "What is the hottest planet in our solar system?", "options": ["Mercury", "Venus", "Mars", "Jupiter"], "answer": "Venus", "difficulty": "medium"},
{"text": "In Roman mythology, who is the god of war?", "options": ["Jupiter", "Neptune", "Mars", "Mercury"], "answer": "Mars", "difficulty": "medium"},
{"text": "What fruit did Persephone eat that forced her to stay in the Underworld for part of the year?", "options": ["Apple", "Pomegranate", "Fig", "Grape"], "answer": "Pomegranate", "difficulty": "medium"},
{"text": "Who was the Greek god of the underworld?", "options": ["Zeus", "Poseidon", "Hades", "Hermes"], "answer": "Hades", "difficulty": "medium"},
{"text": "In Norse mythology, what is the name of the bridge that connects Midgard and Asgard?", "options": ["Bifrost", "Yggdrasil", "Valhalla", "Helheim"], "answer": "Bifrost", "difficulty": "medium"},
{"text": "Which driver is known by the nickname The Iceman?", "options": ["Sebastian Vettel", "Kimi Räikkönen", "Mika Häkkinen", "Valtteri Bottas"], "answer": "Kimi Räikkönen", "difficulty": "medium"},
{"text": "The S Curves (Senna S) are a famous feature of which circuit?", "options": ["Interlagos (Brazil)", "Suzuka (Japan)", "Silverstone (UK)", "Spa (Belgium)"], "answer": "Interlagos (Brazil)", "difficulty": "medium"},
{"text": "Which F1 team is based in Milton Keynes, UK?", "options": ["McLaren", "Williams", "Red Bull Racing", "Mercedes"], "answer": "Red Bull Racing", "difficulty": "medium"},
{"text": "How many gears does a modern (2024) Formula 1 car have?", "options": ["6", "7", "8", "9"], "answer": "8", "difficulty": "medium"},
{"text": "Which tournament is the only Grand Slam played on clay?", "options": ["Australian Open", "French Open", "Wimbledon", "US Open"], "answer": "French Open", "difficulty": "medium"},
{"text": "Who was the first male player to reach 20 Grand Slam titles?", "options": ["Rafael Nadal", "Novak Djokovic", "Roger Federer", "Pete Sampras"], "answer": "Roger Federer", "difficulty": "medium"},
{"text": "What is the name of the team competition in men's tennis?", "options": ["Fed Cup", "Davis Cup", "Laver Cup", "ATP Cup"], "answer": "Davis Cup", "difficulty": "medium"},
{"text": "In which city is the US Open held?", "options": ["Miami", "New York City", "Los Angeles", "Chicago"], "answer": "New York City", "difficulty": "medium"},
{"text": "Who holds the record for the most points scored in a single NBA game (100 points)?", "options": ["Michael Jordan", "Wilt Chamberlain", "Kobe Bryant", "LeBron James"], "answer": "Wilt Chamberlain", "difficulty": "medium"},
{"text": "What is the shot clock duration in an NBA game?", "options": ["20 seconds", "24 seconds", "30 seconds", "35 seconds"], "answer": "24 seconds", "difficulty": "medium"},
{"text": "Which team did Shaquille O'Neal play for when he won three consecutive titles from 2000-2002?", "options": ["Orlando Magic", "Miami Heat", "LA Lakers", "Phoenix Suns"], "answer": "LA Lakers", "difficulty": "medium"},
{"text": "Which NBA legend was known as The Mailman?", "options": ["Scottie Pippen", "Karl Malone", "Charles Barkley", "Patrick Ewing"], "answer": "Karl Malone", "difficulty": "medium"},
{"text": "Who wrote the 1970s hit Bohemian Rhapsody?", "options": ["David Bowie", "Freddie Mercury", "Elton John", "Mick Jagger"], "answer": "Freddie Mercury", "difficulty": "medium"},
{"text": "Which woodwind instrument is often associated with jazz and has a metal body?", "options": ["Clarinet", "Flute", "Saxophone", "Oboe"], "answer": "Saxophone", "difficulty": "medium"},
{"text": "Which female artist released the hit single Like a Virgin in 1984?", "options": ["Cyndi Lauper", "Madonna", "Whitney Houston", "Janet Jackson"], "answer": "Madonna", "difficulty": "medium"},
{"text": "In music theory, what does the term Forte mean?", "options": ["Quiet", "Fast", "Loud", "Slow"], "answer": "Loud", "difficulty": "medium"},
{"text": "Which rapper released the critically acclaimed 2015 album 'To Pimp a Butterfly'?", "options": ["Jay-Z", "Kanye West", "Kendrick Lamar", "Drake"], "answer": "Kendrick Lamar", "difficulty": "medium"},
{"text": "Which desert is the largest hot desert in the world?", "options": ["Gobi", "Kalahari", "Sahara", "Arabian"], "answer": "Sahara", "difficulty": "medium"},
{"text": "The Great Barrier Reef is located off the coast of which country?", "options": ["Brazil", "Australia", "Indonesia", "Thailand"], "answer": "Australia", "difficulty": "medium"},
{"text": "What is the capital of Japan?", "options": ["Kyoto", "Osaka", "Tokyo", "Hiroshima"], "answer": "Tokyo", "difficulty": "medium"},
{"text": "Which mountain range separates Europe and Asia?", "options": ["Andes", "Himalayas", "Ural Mountains", "Alps"], "answer": "Ural Mountains", "difficulty": "medium"},
{"text": "Which country has the largest population in the world (as of 2024)?", "options": ["China", "USA", "India", "Indonesia"], "answer": "India", "difficulty": "medium"},
{"text": "Who wrote the dystopian novel 'Brave New World'?", "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "H.G. Wells"], "answer": "Aldous Huxley", "difficulty": "medium"},
{"text": "In 'The Lord of the Rings', what is the name of the wizard who leads the fellowship?", "options": ["Saruman", "Gandalf", "Radagast", "Albus Dumbledore"], "answer": "Gandalf", "difficulty": "medium"},
{"text": "Which author created the detective character Sherlock Holmes?", "options": ["Agatha Christie", "Arthur Conan Doyle", "Raymond Chandler", "Edgar Allan Poe"], "answer": "Arthur Conan Doyle", "difficulty": "medium"},
{"text": "What is the name of the captain in 'Moby-Dick'?", "options": ["Captain Nemo", "Captain Hook", "Captain Ahab", "Captain Jack Sparrow"], "answer": "Captain Ahab", "difficulty": "medium"},
{"text": "The Renaissance period began in which European country?", "options": ["France", "England", "Italy", "Germany"], "answer": "Italy", "difficulty": "medium"},
{"text": "Which world leader was known as The Iron Lady?", "options": ["Indira Gandhi", "Margaret Thatcher", "Angela Merkel", "Golda Meir"], "answer": "Margaret Thatcher", "difficulty": "medium"},
{"text": "What was the name of the document that ended World War I?", "options": ["Treaty of Ghent", "Treaty of Versailles", "Treaty of Paris", "Treaty of Utrecht"], "answer": "Treaty of Versailles", "difficulty": "medium"},
{"text": "What is the name of the point in an orbit where a satellite is closest to the Earth?", "options": ["Apogee", "Perigee", "Perihelion", "Aphelion"], "answer": "Perigee", "difficulty": "hard"},
{"text": "Which spacecraft was the first to leave the solar system and enter interstellar space?", "options": ["Pioneer 10", "Voyager 1", "Voyager 2", "New Horizons"], "answer": "Voyager 1", "difficulty": "hard"},
{"text": "What is the most abundant element in the Sun by mass?", "options": ["Helium", "Oxygen", "Hydrogen", "Carbon"], "answer": "Hydrogen", "difficulty": "hard"},
{"text": "In Welsh mythology, who is the enchantress who possesses a cauldron of inspiration?", "options": ["Rhiannon", "Cerridwen", "Blodeuwedd", "Arianrhod"], "answer": "Cerridwen", "difficulty": "hard"},
{"text": "In Hindu mythology, which avatar of Vishnu is known as the Lord of the Boar?", "options": ["Varaha", "Kurma", "Narasimha", "Matsya"], "answer": "Varaha", "difficulty": "hard"},
{"text": "What was the name of the shield carried by Athena, often bearing the head of Medusa?", "options": ["Labrys", "Aegis", "Caduceus", "Gungnir"], "answer": "Aegis", "difficulty": "hard"},
{"text": "Who is the only driver to have won the Triple Crown of Motorsport (Monaco GP, Indy 500, Le Mans)?", "options": ["Fernando Alonso", "Graham Hill", "Mario Andretti", "Juan Pablo Montoya"], "answer": "Graham Hill", "difficulty": "hard"},
{"text": "In which year did the Six-Wheeled Tyrrell P34 make its debut in Formula 1?", "options": ["1974", "1976", "1978", "1980"], "answer": "1976", "difficulty": "hard"},
{"text": "Which F1 driver won the 1982 World Championship despite winning only one race?", "options": ["Keke Rosberg", "Nelson Piquet", "Alain Prost", "Niki Lauda"], "answer": "Keke Rosberg", "difficulty": "hard"},
{"text": "Who was the last player to win the Grand Slam (all four majors in a single calendar year) in men's singles?", "options": ["Novak Djokovic", "Roger Federer", "Rod Laver", "Don Budge"], "answer": "Rod Laver", "difficulty": "hard"},
{"text": "In the longest tennis match in history (Isner vs. Mahut, 2010), what was the score of the final set?", "options": ["48-46", "70-68", "64-62", "52-50"], "answer": "70-68", "difficulty": "hard"},
{"text": "Which female player won 13 Grand Slam singles titles before the start of the Open Era?", "options": ["Helen Wills Moody", "Billie Jean King", "Althea Gibson", "Maureen Connolly"], "answer": "Helen Wills Moody", "difficulty": "hard"},
{"text": "Who was the first player in NBA history to record 100 points in a single game?", "options": ["Kareem Abdul-Jabbar", "Wilt Chamberlain", "Elgin Baylor", "Bill Russell"], "answer": "Wilt Chamberlain", "difficulty": "hard"},
{"text": "Which team drafted Kobe Bryant in 1996 before immediately trading him to the Lakers?", "options": ["Charlotte Hornets", "New Jersey Nets", "Orlando Magic", "LA Clippers"], "answer": "Charlotte Hornets", "difficulty": "hard"},
{"text": "What is the name of the trophy awarded to the winner of the NBA Finals?", "options": ["The Naismith Trophy", "The Larry O'Brien Trophy", "The Walter Brown Trophy", "The Stern Cup"], "answer": "The Larry O'Brien Trophy", "difficulty": "hard"},
{"text": "Which famous composer became completely deaf by the time he wrote his Ninth Symphony?", "options": ["Richard Wagner", "Johannes Brahms", "Ludwig van Beethoven", "Franz Schubert"], "answer": "Ludwig van Beethoven", "difficulty": "hard"},
{"text": "In what year did the Woodstock Music & Art Fair take place?", "options": ["1967", "1968", "1969", "1970"], "answer": "1969", "difficulty": "hard"},
{"text": "Which jazz trumpeter recorded the best-selling jazz album of all time, 'Kind of Blue'?", "options": ["Louis Armstrong", "Miles Davis", "Dizzy Gillespie", "Chet Baker"], "answer": "Miles Davis", "difficulty": "hard"},
{"text": "Which country has the most time zones in the world (including its overseas territories)?", "options": ["Russia", "USA", "France", "China"], "answer": "France", "difficulty": "hard"},
{"text": "The Drakensberg mountain range is located primarily in which country?", "options": ["Namibia", "Ethiopia", "South Africa", "Morocco"], "answer": "South Africa", "difficulty": "hard"},
{"text": "What is the name of the world's deepest lake, located in Siberia?", "options": ["Lake Superior", "Lake Tanganyika", "Lake Baikal", "Lake Victoria"], "answer": "Lake Baikal", "difficulty": "hard"},
{"text": "What is the opening line of Herman Melville's 'Moby-Dick'?", "options": ["It was the best of times, it was the worst of times.", "Call me Ishmael.", "All happy families are alike.", "In a hole in the ground there lived a hobbit."], "answer": "Call me Ishmael.", "difficulty": "hard"},
{"text": "Which author wrote the play 'Waiting for Godot'?", "options": ["Eugene O'Neill", "Samuel Beckett", "Tennessee Williams", "Arthur Miller"], "answer": "Samuel Beckett", "difficulty": "hard"},
{"text": "What is the name of the protagonist in Dante Alighieri's 'Divine Comedy'?", "options": ["Virgil", "Beatrice", "Dante", "Ugolino"], "answer": "Dante", "difficulty": "hard"},
{"text": "Which Byzantine Emperor oversaw the construction of the Hagia Sophia?", "options": ["Constantine the Great", "Justinian I", "Theodosius II", "Heraclius"], "answer": "Justinian I", "difficulty": "hard"},
{"text": "The Treaty of Tordesillas (1494) divided the newly discovered lands outside Europe between which two countries?", "options": ["England and France", "Spain and Portugal", "The Netherlands and Spain", "Portugal and Italy"], "answer": "Spain and Portugal", "difficulty": "hard"},
{"text": "Who was the last Tsar of Russia before the 1917 Revolution?", "options": ["Alexander III", "Peter the Great", "Nicholas II", "Ivan the Terrible"], "answer": "Nicholas II", "difficulty": "hard"},
{"text": "What is the only metal that is liquid at standard room temperature?", "options": ["Gallium", "Mercury", "Cesium", "Bromine"], "answer": "Mercury", "difficulty": "hard"},
{"text": "How many hearts does an octopus have?", "options": ["1", "2", "3", "4"], "answer": "3", "difficulty": "hard"},
{"text": "Which letter does not appear in any of the names of the 50 U.S. states?", "options": ["X", "Z", "Q", "J"], "answer": "Q", "difficulty": "hard"},
{"text": "The Hindenburg disaster of 1937 involved an airship filled with which highly flammable gas?", "options": ["Helium", "Methane", "Hydrogen", "Oxygen"], "answer": "Hydrogen", "difficulty": "hard"},
{"text": "What was the magnitude of the 1960 Valdivia earthquake, the strongest ever recorded?", "options": ["8.9", "9.2", "9.5", "9.8"], "answer": "9.5", "difficulty": "hard"},
{"text": "The 1883 eruption of which volcano was so loud it could be heard 3,000 miles away?", "options": ["Mount Pinatubo", "Krakatoa", "Mount Pelée", "Tambora"], "answer": "Krakatoa", "difficulty": "hard"},
{"text": "What was the name of the spacecraft that exploded 73 seconds after liftoff in 1986?", "options": ["Columbia", "Discovery", "Challenger", "Endeavour"], "answer": "Challenger", "difficulty": "hard"},
{"text": "The Black Death plague of the 14th century is estimated to have killed what percentage of Europe's population?", "options": ["10-20%", "30-60%", "70-80%", "90%"], "answer": "30-60%", "difficulty": "hard"},
{"text": "In 1952, the Great Smog caused thousands of deaths in which city due to extreme air pollution?", "options": ["Beijing", "Los Angeles", "London", "Pittsburgh"], "answer": "London", "difficulty": "hard"},
{"text": "Which astronomer first used a telescope to observe the four largest moons of Jupiter?", "options": ["Nicolaus Copernicus", "Johannes Kepler", "Galileo Galilei", "Isaac Newton"], "answer": "Galileo Galilei", "difficulty": "hard"},
{"text": "What is the Chandrasekhar Limit?", "options": ["The speed of light in a vacuum", "The maximum mass of a stable white dwarf star", "The distance to the nearest galaxy", "The temperature of a black hole"], "answer": "The maximum mass of a stable white dwarf star", "difficulty": "hard"},
{"text": "Which spectral class of stars is the hottest?", "options": ["Class M", "Class G", "Class O", "Class A"], "answer": "Class O", "difficulty": "hard"},
{"text": "In Aztec mythology, who is the Plumed Serpent god of wind and wisdom?", "options": ["Huitzilopochtli", "Quetzalcoatl", "Tezcatlipoca", "Tlaloc"], "answer": "Quetzalcoatl", "difficulty": "hard"},
{"text": "According to Greek myth, which Titan was forced to carry the heavens on his shoulders?", "options": ["Prometheus", "Epimetheus", "Atlas", "Cronus"], "answer": "Atlas", "difficulty": "hard"},
{"text": "Who is the father of the Norse god Sleipnir, the eight-legged horse?", "options": ["Odin", "Loki", "Thor", "Heimdall"], "answer": "Loki", "difficulty": "hard"},
{"text": "Which F1 driver holds the record for the most starts without a podium finish (as of 2024)?", "options": ["Adrian Sutil", "Nico Hülkenberg", "Pierluigi Martini", "Marcus Ericsson"], "answer": "Nico Hülkenberg", "difficulty": "hard"},
{"text": "In what year was the first ever Monaco Grand Prix held?", "options": ["1929", "1947", "1950", "1955"], "answer": "1929", "difficulty": "hard"},
{"text": "Who was the designer of the dominant McLaren MP4/4 of 1988?", "options": ["Adrian Newey", "Gordon Murray", "Rory Byrne", "Colin Chapman"], "answer": "Gordon Murray", "difficulty": "hard"},
{"text": "Which player won the 1977 Wimbledon singles title, the centenary year of the tournament?", "options": ["Chris Evert", "Virginia Wade", "Martina Navratilova", "Billie Jean King"], "answer": "Virginia Wade", "difficulty": "hard"},
{"text": "What is the maximum number of sets a women's singles match can go at a Grand Slam?", "options": ["2", "3", "4", "5"], "answer": "3", "difficulty": "hard"},
{"text": "Who is the only tennis player to have won a Golden Slam (all 4 majors and Olympic Gold in one year)?", "options": ["Steffi Graf", "Serena Williams", "Andre Agassi", "Rafael Nadal"], "answer": "Steffi Graf", "difficulty": "hard"},
{"text": "In what year did the 3-point line first introduced to the NBA?", "options": ["1969", "1975", "1979", "1984"], "answer": "1979", "difficulty": "hard"},
{"text": "Which player has won the most NBA MVP awards in history?", "options": ["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Bill Russell"], "answer": "Kareem Abdul-Jabbar", "difficulty": "hard"},
{"text": "What was the final score of the highest-scoring game in NBA history (Detroit vs. Denver, 1983)?", "options": ["186-184", "162-158", "171-166", "155-150"], "answer": "186-184", "difficulty": "hard"},
{"text": "What is the name of the musical structure consisting of an exposition, development, and recapitulation?", "options": ["Rondo", "Fugue", "Sonata Form", "Minuet"], "answer": "Sonata Form", "difficulty": "hard"},
{"text": "Which 20th-century composer wrote the controversial ballet 'The Rite of Spring'?", "options": ["Igor Stravinsky", "Claude Debussy", "Maurice Ravel", "Arnold Schoenberg"], "answer": "Igor Stravinsky", "difficulty": "hard"},
{"text": "Which artist won the first-ever Grammy Award for Album of the Year in 1959?", "options": ["Frank Sinatra", "Henry Mancini", "Ella Fitzgerald", "Perry Como"], "answer": "Henry Mancini", "difficulty": "hard"},
{"text": "What is the only country in the world that has a non-quadrilateral flag?", "options": ["Switzerland", "Nepal", "Bhutan", "Djibouti"], "answer": "Nepal", "difficulty": "hard"},
{"text": "The Danakil Depression, one of the hottest places on Earth, is located in which country?", "options": ["Ethiopia", "Sudan", "Mali", "Yemen"], "answer": "Ethiopia", "difficulty": "hard"},
{"text": "Which river flows through the most countries in the world?", "options": ["Amazon", "Nile", "Danube", "Mekong"], "answer": "Danube", "difficulty": "hard"},
{"text": "In George Orwell's 'Animal Farm', which pig represents Joseph Stalin?", "options": ["Snowball", "Napoleon", "Squealer", "Old Major"], "answer": "Napoleon", "difficulty": "hard"},
{"text": "Who wrote the 14th-century work 'The Canterbury Tales'?", "options": ["Dante Alighieri", "Geoffrey Chaucer", "Giovanni Boccaccio", "Thomas Malory"], "answer": "Geoffrey Chaucer", "difficulty": "hard"},
{"text": "Which novel begins with the line: All children, except one, grow up.?", "options": ["Oliver Twist", "Peter Pan", "Treasure Island", "The Secret Garden"], "answer": "Peter Pan", "difficulty": "hard"},

{"text": "Which film is credited with launching the modern shared cinematic universe trend?", "options": ["The Dark Knight", "Iron Man", "Avengers", "Spider-Man (2002)"], "answer": "Iron Man", "difficulty": "hard"} ,

{"text": "The phrase cinema of attractions is most associated with which era of film?", "options": ["Golden Age Hollywood", "Silent film era", "New Hollywood", "Postmodern cinema"], "answer": "Silent film era", "difficulty": "hard"} , 

{"text": "Which director is known for using non-linear storytelling as a recurring stylistic choice?", "options": ["Steven Spielberg", "Christopher Nolan", "James Cameron", "Ridley Scott"], "answer": "Christopher Nolan", "difficulty": "hard"} ,

{"text": "The Oscars introduced the Best Animated Feature category in which year?", "options": ["1998", "2000", "2001", "2003"], "answer": "2001", "difficulty": "hard"} ,

{"text": "Which movie popularized the concept of the anti-hero in mainstream blockbuster cinema?", "options": ["Joker", "Taxi Driver", "Deadpool", "Fight Club"], "answer": "Fight Club", "difficulty": "hard"} ,

{"text": "Method acting is most closely associated with which acting school?", "options": ["British Academy", "Lee Strasberg Theatre", "Royal Shakespeare Company", "Moscow Art Theatre"], "answer": "Lee Strasberg Theatre", "difficulty": "hard"} ,

{"text": "Which film was the first non-English language movie to win Best Picture at the Oscars?", "options": ["Roma", "Parasite", "Amour", "Crouching Tiger, Hidden Dragon"], "answer": "Parasite", "difficulty": "hard"} ,

{"text": "Auteur theory primarily emphasizes the role of the:", "options": ["Producer", "Screenwriter", "Director", "Cinematographer"], "answer": "Director", "difficulty": "hard"} ,

{"text": "Which genre revival was largely driven by Quentin Tarantino's early work?", "options": ["Western", "Slasher", "Crime pulp", "Science fiction"], "answer": "Crime pulp", "difficulty": "hard"} ,

{"text": "CGI became mainstream in Hollywood after which film's success?", "options": ["Jurassic Park", "Titanic", "Terminator 2", "Star Wars"], "answer": "Jurassic Park", "difficulty": "hard"} ,

{"text": "Which term refers to movies designed mainly for award recognition?", "options": ["Blockbusters", "Indie films", "Oscar bait", "Art house cinema"], "answer": "Oscar bait", "difficulty": "hard"} ,

{"text": "The Marvel Phase structure is primarily a strategy for:", "options": ["Budget management", "Narrative continuity", "Marketing releases", "Fan service"], "answer": "Narrative continuity", "difficulty": "hard"} ,

{"text": "Which film movement emphasized realism and non-professional actors?", "options": ["German Expressionism", "Italian Neorealism", "French New Wave", "New Hollywood"], "answer": "Italian Neorealism", "difficulty": "hard"} ,

{"text": "Which movie is often cited as the first cult classic?", "options": ["Rocky Horror Picture Show", "Citizen Kane", "Blade Runner", "Clockwork Orange"], "answer": "Rocky Horror Picture Show", "difficulty": "hard"} ,

{"text": "What does the term 'reboot' imply in pop culture?", "options": ["Continuation", "Alternate ending", "Franchise restart", "Spin-off"], "answer": "Franchise restart", "difficulty": "hard"} ,

{"text": "Which director is famous for symmetrical framing and pastel color palettes?", "options": ["David Fincher", "Wes Anderson", "Tim Burton", "Paul Thomas Anderson"], "answer": "Wes Anderson", "difficulty": "hard"} ,

{"text": "Box office numbers adjusted for inflation place which film at #1?", "options": ["Avatar", "Titanic", "Avengers: Endgame", "Gone with the Wind"], "answer": "Gone with the Wind", "difficulty": "hard"} ,

{"text": "Which award is considered the highest honor at Cannes Film Festival?", "options": ["Golden Globe", "Palme d'Or", "Golden Bear", "Lion d'Oro"], "answer": "Palme d'Or", "difficulty": "hard"} ,

{"text": "Which movie popularized post-credit scenes?", "options": ["Avengers", "Iron Man", "Ferris Bueller", "Guardians of the Galaxy"], "answer": "Iron Man", "difficulty": "hard"} ,

{"text": "The 'found footage' horror genre gained mainstream popularity after?", "options": ["Paranormal Activity", "Blair Witch Project", "REC", "Cloverfield"], "answer": "Blair Witch Project", "difficulty": "hard"} ,

{"text": "Which term describes excessive nostalgia-driven content?", "options": ["Retro-core", "Fan service", "Rehash culture", "Pop recycling"], "answer": "Fan service", "difficulty": "hard"} ,

{"text": "Which film is studied extensively for unreliable narration?", "options": ["Memento", "Inception", "Shutter Island", "Donnie Darko"], "answer": "Memento", "difficulty": "hard"} ,

{"text": "Which actor has won the most Oscars for acting?", "options": ["Daniel Day-Lewis", "Jack Nicholson", "Katharine Hepburn", "Meryl Streep"], "answer": "Katharine Hepburn", "difficulty": "hard"} ,

{"text": "Which streaming service disrupted traditional theatrical windows first?", "options": ["Amazon Prime", "Netflix", "Hulu", "Disney+"], "answer": "Netflix", "difficulty": "hard"} ,

{"text": "Which genre dominates global box offices post-2010?", "options": ["Romance", "Comedy", "Superhero", "Western"], "answer": "Superhero", "difficulty": "hard"} ,

{"text": "The term binge-watching gained popularity due to which platform?", "options": ["HBO", "Netflix", "Amazon", "Hulu"], "answer": "Netflix", "difficulty": "hard"} ,

{"text": "Which TV show is considered the start of prestige television?", "options": ["Friends", "The Sopranos", "Lost", "Seinfeld"], "answer": "The Sopranos", "difficulty": "hard"} ,

{"text": "Cliffhangers are mainly used to:", "options": ["Increase runtime", "Retain viewership", "Reduce budget", "End seasons"], "answer": "Retain viewership", "difficulty": "hard"} ,

{"text": "Which show redefined anti-hero protagonists on TV?", "options": ["Dexter", "Breaking Bad", "Mad Men", "House of Cards"], "answer": "Breaking Bad", "difficulty": "hard"} ,

{"text": "Sitcoms traditionally use which format?", "options": ["Single-camera", "Multi-camera", "Hand-held", "Documentary"], "answer": "Multi-camera", "difficulty": "hard"} ,

{"text": "Which series popularized the cold open format?", "options": ["The Office", "Friends", "Parks and Rec", "HIMYM"], "answer": "The Office", "difficulty": "hard"} ,

{"text": "The phrase Peak TV refers to:", "options": ["Reality shows", "Maximum content production", "Award-winning era", "Decline of cable"], "answer": "Maximum content production", "difficulty": "hard"} ,

{"text": "Which show had the most expensive final season?", "options": ["Breaking Bad", "Stranger Things", "Game of Thrones", "The Crown"], "answer": "Game of Thrones", "difficulty": "hard"} ,

{"text": "Reality TV relies heavily on which element?", "options": ["Scripted dialogue", "Post-production editing", "CGI", "Voice acting"], "answer": "Post-production editing", "difficulty": "hard"} ,

{"text": "Which streaming trend changed weekly episode releases?", "options": ["Pilot drops", "Full-season releases", "Miniseries format", "Live streaming"], "answer": "Full-season releases", "difficulty": "hard"} ,

{"text": "Which show is often cited as the most pirated in history?", "options": ["Breaking Bad", "Game of Thrones", "Stranger Things", "The Walking Dead"], "answer": "Game of Thrones", "difficulty": "hard"} ,

{"text": "Anthology series differ because they:", "options": ["Continue same story", "Change characters each season", "Focus on comedy", "Are unscripted"], "answer": "Change characters each season", "difficulty": "hard"} ,

{"text": "Which genre dominates reality TV globally?", "options": ["Survival", "Dating", "Talent competitions", "Game shows"], "answer": "Talent competitions", "difficulty": "hard"} ,

{"text": "The rise of OTT platforms caused a decline in?", "options": ["Film budgets", "Cable TV viewership", "Indie cinema", "Awards"], "answer": "Cable TV viewership", "difficulty": "hard"} ,

{"text": "Which show popularized mockumentary style?", "options": ["Friends", "Seinfeld", "The Office", "Scrubs"], "answer": "The Office", "difficulty": "hard"} ,

{"text": "Streaming algorithms primarily affect:", "options": ["Content quality", "Viewer recommendations", "Production budgets", "Episode length"], "answer": "Viewer recommendations", "difficulty": "hard"} ,

{"text": "Limited series differ from regular series by:", "options": ["Budget", "Episode count fixed", "Genre", "Platform"], "answer": "Episode count fixed", "difficulty": "hard"} ,

{"text": "Which TV trend emphasizes diversity and representation?", "options": ["Colorblind casting", "Inclusive storytelling", "Prestige TV", "Fan service"], "answer": "Inclusive storytelling", "difficulty": "hard"} ,

{"text": "Which show redefined fantasy TV ,production scale?", "options": ["The Witcher", "Game of Thrones", "Vikings", "Rings of Power"], "answer": "Game of Thrones", "difficulty": "hard"} ,

{"text": "Which metric determines streaming success most?", "options": ["Reviews", "Completion rate", "Ratings", "Box office"], "answer": "Completion rate", "difficulty": "hard"} ,

{"text": "The term \u201cshowrunner\u201d refers to the:", "options": ["Director", "Producer-writer head", "Actor lead", "Studio executive"], "answer": "Producer-writer head", "difficulty": "hard"} ,

{"text": "Which show was Netflix\u2019s first original hit?", "options": ["Orange Is the New Black", "House of Cards", "Narcos", "Daredevil"], "answer": "House of Cards", "difficulty": "hard"} ,

{"text": "Reboots on TV often target which audience?", "options": ["New viewers only", "Nostalgic fans", "Critics", "Award juries"], "answer": "Nostalgic fans", "difficulty": "hard"} ,

{"text": "Which format thrives on social media discussion?", "options": ["Sitcom", "Weekly episodic shows", "Miniseries", "Reality documentaries"], "answer": "Weekly episodic shows", "difficulty": "hard"} ,

{"text": "Which trend dominates Gen-Z TV consumption?", "options": ["Cable", "Late-night shows", "Short-form content", "Soap operas"], "answer": "Short-form content", "difficulty": "hard"} ,

{"text": "The shift from albums to singles was driven by?", "options": ["Radio", "Streaming platforms", "Vinyl revival", "Record labels"], "answer": "Streaming platforms", "difficulty": "hard"} ,

{"text": "Which genre dominates TikTok virality?", "options": ["Jazz", "Rock", "Pop & Hip-hop", "Classical"], "answer": "Pop & Hip-hop", "difficulty": "hard"} ,

{"text": "Fanbases named after artists signify:", "options": ["Marketing", "Brand loyalty", "Cultural identity", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which artist redefined surprise album drops?", "options": ["Drake", "Beyonce", "Kanye West", "Rihanna"], "answer": "Beyonce", "difficulty": "hard"} ,

{"text": "Music charts today prioritize:", "options": ["Album sales", "Streaming numbers", "Radio plays", "Physical copies"], "answer": "Streaming numbers", "difficulty": "hard"} ,

{"text": "Which term describes online fan conflict?", "options": ["Cancel culture", "Stan wars", "Meme fights", "Culture clash"], "answer": "Stan wars", "difficulty": "hard"} ,

{"text": "Meme longevity depends on?", "options": ["Humor", "Relatability", "Platform algorithms", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which decade shaped modern pop culture most?", "options": ["1960s", "1980s", "1990s", "2010s"], "answer": "2010s", "difficulty": "hard"} ,

{"text": "Cancel culture originated mainly from?", "options": ["Television", "Social media", "Newspapers", "Radio"], "answer": "Social media", "difficulty": "hard"} ,

{"text": "Which platform accelerated influencer culture?", "options": ["Facebook", "Instagram", "Twitter", "Reddit"], "answer": "Instagram", "difficulty": "hard"} ,

{"text": "Viral trends are best described as:", "options": ["Planned campaigns", "Organic mass participation", "Advertisements", "News events"], "answer": "Organic mass participation", "difficulty": "hard"} ,

{"text": "Remix culture thrives due to?", "options": ["Copyright law", "Fan creativity", "Algorithm support", "B and C"], "answer": "B and C", "difficulty": "hard"} ,

{"text": "Which music award is fan-voted primarily?", "options": ["Grammy", "Billboard", "MTV VMAs", "Oscars"], "answer": "MTV VMAs", "difficulty": "hard"} ,

{"text": "Which pop culture form spreads fastest today?", "options": ["Films", "Music", "Memes", "TV shows"], "answer": "Memes", "difficulty": "hard"} ,

{"text": "Which phenomenon reflects parasocial relationships?", "options": ["Fan fiction", "Celebrity worship", "Influencer culture", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which artist blurred genre boundaries most in the 2010s?", "options": ["Adele", "Billie Eilish", "Bruno Mars", "Ed Sheeran"], "answer": "Billie Eilish", "difficulty": "hard"} ,

{"text": "Internet slang becomes mainstream through?", "options": ["Academia", "Youth culture", "Advertisements", "News media"], "answer": "Youth culture", "difficulty": "hard"} ,

{"text": "Which platform popularized reaction culture?", "options": ["TikTok", "YouTube", "Instagram", "Snapchat"], "answer": "YouTube", "difficulty": "hard"} ,

{"text": "Which trend revived vinyl records?", "options": ["Nostalgia marketing", "Audiophile culture", "Collectibility", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Fandom toxicity often arises from?", "options": ["Platform bias", "Identity attachment", "Competition", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which music genre heavily influences fashion trends?", "options": ["Classical", "Hip-hop", "Jazz", "Folk"], "answer": "Hip-hop", "difficulty": "hard"} ,

{"text": "The term mainstream implies?", "options": ["Artistic purity", "Mass appeal", "Niche content", "Underground culture"], "answer": "Mass appeal", "difficulty": "hard"} ,

{"text": "Which pop trend reflects globalization most?", "options": ["Hollywood remakes", "K-Pop", "Sitcoms", "Reality TV"], "answer": "K-Pop", "difficulty": "hard"} ,

{"text": "Fan edits primarily exist due to?", "options": ["Software access", "Emotional investment", "Platform reach", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which factor most influences pop culture longevity?", "options": ["Quality", "Accessibility", "Relatability", "Timing"], "answer": "Relatability", "difficulty": "hard"} ,

{"text": "Stan culture originated from?", "options": ["Hip-hop slang", "Eminem song", "Twitter", "Tumblr"], "answer": "Eminem song", "difficulty": "hard"} ,

{"text": "Which decade introduced meme culture widely?", "options": ["1990s", "2000s", "2010s", "2020s"], "answer": "2010s", "difficulty": "hard"} ,

{"text": "Influencer marketing works because of?", "options": ["Trust", "Reach", "Authenticity perception", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which art form merges fandom and creativity?", "options": ["Fan fiction", "Fan art", "Cosplay", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which platform emphasizes short-form cultural trends most?", "options": ["YouTube", "TikTok", "Netflix", "Spotify"], "answer": "TikTok", "difficulty": "hard"} ,

{"text": "Pop culture is best defined as?", "options": ["Elite culture", "Mass-consumed culture", "Academic culture", "Traditional culture"], "answer": "Mass-consumed culture", "difficulty": "hard"} ,

{"text": "Which trend challenges traditional celebrity status?", "options": ["Influencers", "Paparazzi", "Award shows", "Studios"], "answer": "Influencers", "difficulty": "hard"} ,

{"text": "Which factor fuels virality fastest?", "options": ["Humor", "Shock value", "Emotional response", "Consistency"], "answer": "Emotional response", "difficulty": "hard"} ,

{"text": "Which medium dominates Gen-Alpha culture?", "options": ["TV", "Films", "Mobile content", "Print"], "answer": "Mobile content", "difficulty": "hard"} ,

{"text": "Which pop culture cycle is shortest today?", "options": ["Fashion", "Music trends", "Internet memes", "Film genres"], "answer": "Internet memes", "difficulty": "hard"} ,

{"text": "Which term describes online trend exhaustion?", "options": ["Burnout", "Trend fatigue", "Overexposure", "Saturation"], "answer": "Trend fatigue", "difficulty": "hard"} ,

{"text": "Which cultural shift enabled creator economy?", "options": ["Smartphones", "Social platforms", "Monetization tools", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which pop trend relies most on nostalgia?", "options": ["Reboots", "Remakes", "Sequels", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which platform blurred lines between audience and creator?", "options": ["Instagram", "YouTube", "TikTok", "Twitter"], "answer": "TikTok", "difficulty": "hard"} ,

{"text": "Which element defines cult fandoms most?", "options": ["Size", "Passion", "Media coverage", "Awards"], "answer": "Passion", "difficulty": "hard"} ,

{"text": "Which trend reflects attention economy?", "options": ["Clickbait", "Short videos", "Viral hooks", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which pop form spreads globally fastest?", "options": ["Cinema", "Music", "Internet memes", "Television"], "answer": "Internet memes", "difficulty": "hard"} ,

{"text": "Which phenomenon shows pop culture commodification?", "options": ["Merchandising", "Brand collaborations", "Sponsored content", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which audience influences trends the most today?", "options": ["Boomers", "Gen-X", "Millennials", "Gen-Z"], "answer": "Gen-Z", "difficulty": "hard"} ,

{"text": "Which medium shapes identity expression most?", "options": ["TV", "Music", "Social media", "Films"], "answer": "Social media", "difficulty": "hard"} ,

{"text": "Which pop culture shift reduced gatekeeping?", "options": ["Streaming", "Social platforms", "DIY creation", "All of the above"], "answer": "All of the above", "difficulty": "hard"} ,

{"text": "Which trend represents pop culture fragmentation?", "options": ["Mass media", "Niche fandoms", "Award shows", "Cable TV"], "answer": "Niche fandoms", "difficulty": "hard"} ,

{"text": "Which metric defines modern popularity?", "options": ["Sales", "Views", "Engagement", "Awards"], "answer": "Engagement", "difficulty": "hard"} ,

{"text": "Which factor sustains pop icons long-term?", "options": ["Talent", "Reinvention", "Marketing", "Controversy"], "answer": "Reinvention", "difficulty": "hard"} ,

{"text": "Pop culture ultimately reflects?", "options": ["Elite values", "Government policy", "Collective social behavior", "Academic theory"], "answer": "Collective social behavior", "difficulty": "hard"} ,
]

def clear_and_upload():
    print("Deleting old questions...")
    docs = db.collection("questions").stream()
    for doc in docs:
        doc.reference.delete()
    
    print("Uploading 150 questions...")
    for q in questions_to_add:
        # --- PASTE THE SAFETY CHECK HERE ---
        if q['answer'] not in q['options']:
            print(f"⚠️ SKIPPING: Answer '{q['answer']}' is not in options for: {q['text'][:30]}...")
            continue 
        # ------------------------------------

        # Create a unique ID to prevent duplicates
        doc_id = hashlib.md5(q['text'].encode()).hexdigest()[:16]
        db.collection("questions").document(doc_id).set(q)
    
    print("Done! Database is refreshed.")

if __name__ == "__main__":
    clear_and_upload()