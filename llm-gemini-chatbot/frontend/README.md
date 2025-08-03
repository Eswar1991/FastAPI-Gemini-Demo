Természetesen! Íme egy módosított README fájl, amely a korábbi Create React App alapú leírást úgy igazítja, hogy illeszkedjen az Ön FastAPI + Google Gemini backend és React chat UI architektúrájához.

# LLM-Chatbot with FastAPI Backend and React Frontend (Gemini-powered)

This project demonstrates a simple full-stack chatbot application, where:

- **Backend:** FastAPI microservice using Google Gemini LLM for generating essays and poems.
- **Frontend:** React-based chat UI that communicates with the backend via HTTP.

## Available Scripts

You can run these scripts separately in the frontend and backend directories.

### Backend Setup (FastAPI + Gemini)

In the backend directory (`backend/`):

- Make sure you have your `.env` file with your Gemini API key:

  ```
  GEMINI_API_KEY=your_actual_gemini_api_key_here
  ```

- Install Python dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- Run the FastAPI server (default on localhost:8000):

  ```bash
  python -m app.main
  ```

The backend exposes endpoints like:

- `/essay-direct?topic=YOUR_TOPIC` — generates an essay.
- `/poem-direct?topic=YOUR_TOPIC` — generates a poem.

### Frontend Setup (React Chat UI)

In the frontend directory (`frontend/`):

- Install Node.js dependencies:

  ```bash
  npm install
  ```

- Start the React development server:

  ```bash
  npm start
  ```

This will launch the React app at [http://localhost:3000](http://localhost:3000).

### How It Works

- You type a topic/message in the chat UI.
- Select whether you want to generate an essay or poem.
- The React frontend sends a request to the corresponding FastAPI endpoint (`/essay-direct` or `/poem-direct`).
- The response is displayed in the chat interface.

### More Scripts (Frontend)

These available npm scripts help manage the React app lifecycle:

#### `npm start`

Runs the app in development mode.  
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page reloads on changes and shows lint errors in the console.

#### `npm test`

Launches the test runner in interactive watch mode.  
See more: [running tests](https://facebook.github.io/create-react-app/docs/running-tests)

#### `npm run build`

Builds the app for production in the `build` folder with optimized bundles.  
Your app is ready for deployment!

See more: [deployment](https://facebook.github.io/create-react-app/docs/deployment)

#### `npm run eject`

**Warning: this is a one-way operation!**

Ejecting exposes the build configuration and dependencies for full customization. Use only if necessary.

### Notes

- The React app uses `"proxy": "http://localhost:8000"` for API calls during development.
- Make sure your FastAPI server is running before starting React, so API requests succeed.
- You can modify the endpoints or UI logic to extend functionality.
- This setup uses Google Gemini models via the official `google-genai` SDK in backend.
- Manage sensitive API keys securely via `.env` files — do not commit them!

### Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [Create React App Documentation](https://facebook.github.io/create-react-app/docs/getting-started)
- [Google Gemini API Docs](https://developers.generativeai.google/)

# Summary

This repo combines:

- A **FastAPI backend** exposing simple text generation endpoints powered by Google Gemini.
- A **React frontend** chatbot UI calling backend API endpoints, allowing users to request essays or poems interactively.

Run backend and frontend separately, as described above, and start chatting with your AI!


[1] https://github.com/facebook/create-react-app