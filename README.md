# Flask MongoDB Application

A complete full-stack web application that demonstrates building a Flask API, form submission, and MongoDB integration.

## 📌 What This Project Does

### 1. Backend API Endpoint (`/api`)
- Reads data from `data/products.json` file
- Returns JSON list of 5 products
- Demonstrates backend data serving

### 2. Frontend Form
- User-friendly form with validation
- Fields: Name, Email, Phone (required), Message (optional)
- Responsive design that works on all devices
- Real-time API data fetching

### 3. MongoDB Storage
- Submits form data to MongoDB Atlas
- Stores in `new1` database, `submissions` collection
- Auto-generates timestamps for each submission

### 4. Success/Error Handling
- ✅ **Success**: Redirects to success page
- ❌ **Error**: Shows error message on same page (no redirect)
- Form validation with clear user messages

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Application
```bash
python app.py
```

### 3. Open in Browser
- Form: http://127.0.0.1:5000
- API: http://127.0.0.1:5000/api

## 📁 Project Files

```
flask-mongodb-app/
├── app.py                  # Flask application (92 lines)
├── requirements.txt        # Python packages
├── data/
│   └── products.json      # 5 sample products
└── templates/
    ├── index.html         # Form page
    └── success.html       # Success page
```

## 🔌 API Endpoints

| Method | URL | Purpose |
|--------|-----|---------|
| GET | `/` | Form page |
| GET | `/api` | Get products (JSON) |
| POST | `/submit` | Submit form |
| GET | `/success` | Success page |
| GET | `/submissions` | View all submissions |

## � Screenshots

### API Data Test
Shows the application fetching and displaying JSON data from the backend API endpoint.

![API Data Test](screenshots/1%20(1).png)

### Form Submission
Shows the complete form with validation fields (Name, Email, Phone) and message input ready for MongoDB submission.

![Form Submission](screenshots/1%20(2).png)

### Success Page
Shows the success confirmation page after form submission with submission details.

![Success Page](screenshots/1%20(3).png)

### View All Submissions
Shows the MongoDB submissions view with all stored data.

![Submissions](screenshots/1%20(4).png)

## �📝 How to Use

### Getting API Data
Open http://127.0.0.1:5000/api to see:
```json
{
  "products": [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics", "inStock": true},
    {"id": 2, "name": "Wireless Mouse", "price": 29.99, "category": "Accessories", "inStock": true},
    {...}
  ]
}
```

### Submitting the Form
1. Open http://127.0.0.1:5000
2. Click "Fetch API Data" to see products
3. Fill required fields: Name, Email, Phone
4. Optional: Add message
5. Click Submit Data
6. Success: Redirected to success page
7. Error: Message stays on form

### Viewing Submissions
- Click "View All Submissions" on success page
- Or visit http://127.0.0.1:5000/submissions

## 💾 MongoDB Details

**Connection**: `mongodb+srv://nomanqadri34:U0hSWV1mHsiR7PJo@cluster1.xhpp5nd.mongodb.net/new1`

**Database**: `new1`  
**Collection**: `submissions`

**Stored Data**:
```javascript
{
  "_id": ObjectId(),
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "message": "Optional message",
  "submitted_at": "2026-02-21T15:30:45.123456"
}
```

## 🛠️ Technologies Used

| Component | Technology | Version |
|-----------|-----------|---------|
| Backend | Flask | 2.3.3 |
| Database | MongoDB Atlas | Latest |
| Driver | PyMongo | 4.5.0 |
| Frontend | HTML5/CSS3/JS | Native |
| Server | Werkzeug | 3.1.6 |

## ✅ Features

- ✓ Reads JSON data from backend file
- ✓ Serves data via REST API
- ✓ Form validation (required fields)
- ✓ MongoDB data storage
- ✓ Auto-generated timestamps
- ✓ Success page redirect
- ✓ Error display on same page
- ✓ Responsive design
- ✓ Professional styling
- ✓ Error handling

## 🧪 Testing

### Test 1: Check API
- Open http://127.0.0.1:5000/api
- Should see 5 products in JSON format

### Test 2: Form Validation
- Leave fields empty and click Submit
- Should see error message (no redirect)

### Test 3: Successful Submit
- Fill Name, Email, Phone fields
- Click Submit
- Should redirect to success page
- Data should appear in MongoDB

### Test 4: View Submissions
- On success page, click "View All Submissions"
- Should display all submitted data

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 5000 in use | `taskkill /PID <id> /F` then run app again |
| MongoDB not connecting | Check internet, verify credentials, check IP whitelist |
| Form won't submit | Open DevTools (F12), check console for errors |
| API returns 404 | Check `data/products.json` exists and is valid JSON |

## 📦 Dependencies

```
Flask==2.3.3
pymongo==4.5.0
python-dotenv==1.0.0
```

## 🔐 Security

For production, use environment variables for MongoDB credentials:
```python
import os
from dotenv import load_dotenv
load_dotenv()
MONGODB_URI = os.getenv('MONGODB_URI')
```

Create `.env` file:
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database
```

## 📖 Code Structure

**app.py** - Main application
- Import Flask and MongoDB
- Configure routes
- Handle form submission
- Connect to database
- Validate input
- Return responses

**index.html** - Form page
- HTML form structure
- CSS styling
- JavaScript for API fetch
- Error display
- Responsive layout

**success.html** - Success page
- Success message
- Submission details
- Timestamp display
- View all button
- Back to form link

**products.json** - Data file
- 5 sample products
- Fields: id, name, price, category, inStock

## 🚀 Deployment

### Heroku
1. Create `Procfile`: `web: python app.py`
2. Create `runtime.txt`: `python-3.9.0`
3. Push: `git push heroku main`

### Local Server
- Already running at http://127.0.0.1:5000
- Debug mode enabled
- Auto-restart on code changes

## 📚 Learning This Code

This project teaches:
- Building REST APIs with Flask
- Reading/parsing JSON files
- HTML form submission
- Form validation
- MongoDB integration
- Frontend-backend communication
- Error handling
- Responsive web design
- Database operations

## 💬 Support

**Issues?**
1. Check Flask/PyMongo documentation
2. Verify MongoDB Atlas connection
3. Check browser console (F12)
4. Review error messages

**GitHub**: https://github.com/nomanqadri34/Flask-and-mongodb

## ✨ Summary

This is a complete, working Flask application that:
- ✓ Serves JSON data from a file
- ✓ Has a functional form for data input
- ✓ Stores data in MongoDB
- ✓ Shows success/error messages correctly
- ✓ Works responsively on all devices
- ✓ Includes proper error handling

Ready to use, modify, and deploy!

---

**Status**: Production Ready ✅  
**Version**: 1.0  
**Updated**: February 21, 2026
