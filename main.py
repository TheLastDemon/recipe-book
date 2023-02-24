from app.configuration import app
import redis

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3057, debug=True)
