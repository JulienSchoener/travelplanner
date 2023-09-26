# 🌍 Travel Planner ✈️

Welcome to Travel Planner, your new travel companion! It's your personal schedule assistant in one place. Say goodbye to the stress of juggling multiple apps and websites. Your flights, hotel bookings, and meetings can now all be managed seamlessly from one central location and shared with business partners. 

## 🚀 Features

- **Flights**: Add, update, and delete flights. Never miss a flight again with our smart validation that ensures your departure times are always after your arrival times.
- **Hotel Bookings**: Manage all your hotel bookings. Keep track of check-in and check-out times and never worry about overbooking.
- **Meetings**: Schedule and manage all your meetings with business partners. Keep everything organized and in one place.
- **Business Partner Schedule**: View the detailed schedule of your business partners, including flights, hotel bookings, and meetings.
- **Responsive Design**: Access your travel planner on any device. It's designed to work beautifully on desktop, tablet, and mobile.

## 💡 Getting Started

### Installation

1. Clone the repository:
```
git clone https://github.com/JulienSchoener/travelplanner.git
```

2. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Create a `.env` file in the base directory with the following variables:
```
SECRET_KEY=your_secret_key
db_name=your_db_name
db_user=your_db_user
db_pwd=your_db_password
db_host=your_db_host
db_port=your_db_port
```

5. Run the migrations:
```
python manage.py migrate
```

6. Run the server:
```
python manage.py runserver
```

Open your web browser and go to `http://127.0.0.1:8000/`.

### Usage

1. **Home Page**: The home page displays the schedule of a specific business partner.
2. **Business Partner Schedule**: This page displays the flights, hotel bookings, and meetings of a specific business partner.
3. **Add Business Partner**: This page allows you to add a new business partner.

## 🤝 Contributing

We welcome contributions of all kinds from the community. Whether you're fixing a bug, adding a new feature, or updating documentation, your efforts are much appreciated! 

## 📜 License

This project is licensed under the MIT License. 
