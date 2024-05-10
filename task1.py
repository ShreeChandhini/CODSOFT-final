# User input
print("Warm Greetings!")
user_input = input("Ask me something: ")

# Check for specific queries
if 'Weather in Chennai' in user_input:
    print("Oh, in Chennai, it's currently sunny and warm! Enjoy the beautiful weather!")
elif 'Good restaurant in Chennai' in user_input:
    print("Absolutely! If you’re looking for a delicious dining experience in Chennai, I highly recommend trying ‘Dakshin’ at the Crowne Plaza Hotel. They serve authentic South Indian cuisine that will tantalize your taste buds!")
elif 'Popular tourist attractions in Chennai?' in user_input:
    print("Oh, there are quite a few popular tourist attractions in Chennai! Marina Beach is a must-visit, known for its beautiful sandy shores and stunning sunsets. Another great spot is the Kapaleeshwarar Temple, a magnificent Hindu temple with intricate architecture. Don’t forget to explore the historic Fort St. George as well, it’s the oldest English fortress in India!")
elif 'Famous museums in Chennai' in user_input:
    print("Absolutely! Chennai is home to some fascinating museums. One of the most famous ones is the Government Museum, also known as the Madras Museum. It houses a diverse collection of art, archaeology, and natural history exhibits. Another notable museum is the Birla Planetarium, where you can explore the wonders of the universe through captivating shows and interactive displays!")
elif 'Popular shopping destinations in Chennai' in user_input:
    print("Oh, there are plenty of great places to shop in Chennai! One popular destination is Express Avenue, a huge shopping mall with a wide range of stores and entertainment options. Another favorite among locals and tourists is T Nagar, known for its bustling street markets where you can find everything from clothing to jewelry. Don’t miss out on Phoenix Marketcity either, it’s a massive mall with a fantastic selection of shops and restaurants!")
elif 'Best time to visit Chennai' in user_input:
    print("The best time to visit Chennai is during the winter months, from November to February. The weather is pleasant and the temperatures are cooler, making it ideal for exploring the city and its attractions. You’ll also get to enjoy festivals like Pongal during this time. Just remember to pack some light sweaters or jackets for the evenings!")
elif 'Tourism in Chennai' in user_input:
    print("There are so many amazing places to explore! You could start with a visit to the beautiful Marina Beach, the second-longest urban beach in the world. Another must-see is the iconic Kapaleeshwarar Temple, known for its stunning Dravidian architecture. For history buffs, the Government Museum is a great place to learn about the rich cultural heritage of the region. And if you’re interested in art, the DakshinaChitra Museum showcases traditional South Indian art and culture. Enjoy your time exploring Chennai!")
elif 'Good Movies in Chennai' in user_input:
    print("There are many great movies that you can watch in Chennai! Some popular ones include “Kaithi,” a Tamil action thriller, and “Super Deluxe,” a Tamil dark comedy-drama. If you’re in the mood for a feel-good romantic film, “96” is a highly recommended choice. And if you’re interested in historical dramas, “Baahubali: The Beginning” and “Baahubali: The Conclusion” are epic movies that are definitely worth watching. Enjoy the movie night!")
elif 'Best Things in Chennai' in user_input:
    print("There are so many wonderful things to experience in Chennai! You can explore the historic Fort St. George, visit the vibrant and bustling markets like Pondy Bazaar and T Nagar, and indulge in delicious South Indian cuisine at places like Murugan Idli Shop or Saravana Bhavan. Don’t forget to check out the beautiful temples like Kapaleeshwarar Temple and the serene Theosophical Society. And of course, the beaches like Marina Beach and Elliot’s Beach are perfect for a relaxing stroll. Chennai has it all!")
elif 'Chennai Known for' in user_input:
    print("Chennai is known for its rich cultural heritage, beautiful temples, and vibrant arts scene. It is often referred to as the “Gateway to South India” and is famous for its traditional Tamil architecture and cuisine. The city is also known for its long coastline, with Marina Beach being a popular attraction. Chennai is a hub for the Tamil film industry, known as Kollywood, and hosts various cultural festivals throughout the year. Overall, Chennai is a city that beautifully blends tradition and modernity. It's a place where you can experience the charm of South Indian culture.")
else:
    # Default response
    print("I'm sorry, I don't have the answer to that question.")