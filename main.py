from app.configuration import app
import redis

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3057, debug=True)

    # r = redis.StrictRedis(
    #     host="c-c9q390bb2d0v3okhrc2c.rw.mdb.yandexcloud.net",
    #     password="rezina675",
    # )
    #
    # r.set("foo", "bar")
    # print(r.get("foo"))
