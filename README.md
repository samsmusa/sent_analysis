# Sentiment Analysis

This is a FastAPI application that performs sentiment analysis on text data. It provides a simple API for analyzing the sentiment of text inputs. <br>
### Front-end(ReactJS)
Find component inside
> @user:~$ ./root/app/templates/assets/js/src

see Sentiment analysis model  [https://huggingface.co/StatsGary/setfit-ft-sentinent-eval](https://huggingface.co/StatsGary/setfit-ft-sentinent-eval)
## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/samsmusa/sentiment_analysis_v1.git
   ```

2. Change into the project directory:

   ```bash
   cd sentiment_analysis_v1
   ```
   
3. Create python virtual environment
    ```bash
    ptyhon3 -m venv env 
    ```
4. Activate Virtual environment
    ```bash
    source env/bin/activate
   ```
5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the FastAPI application, run the following command:

### run from root dir and also collect logs

```bash
python run.py
```
### or

```bash
uvicorn app.main:app --reload --port 8000
```

This command uses [uvicorn](https://www.uvicorn.org/) to run the application with automatic reloading enabled.

The application will be accessible at `http://localhost:8000`.
![browser](https://raw.githubusercontent.com/samsmusa/sent_analysis/main/Screenshot%20from%202023-06-20%2014-04-04.png)

### Documentation
find swagger documentation , browse
`http://localhost:8000/docs`.

### API Endpoints

#### POST /analyze

Analyze the sentiment of a text input.

- Request Body:
  - `text` (string): The text input to analyze.

- Response:
  - `sentiment` (string): The sentiment of the text input. Possible values are "positive", "negative", or "neutral".

Example cURL command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "I love this product!"}' http://localhost:8000/analyze
```

Example response:

```json
{
  "sentiment": "positive",
  "value": 1
}
```

## Deployment

This application can be deployed using [Vercel](https://vercel.com/) or any other hosting platform that supports Python applications. Refer to the [Deployment Guide](https://vercel.com/guides/deploying-fastapi-to-vercel) for deploying a FastAPI application to Vercel.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
