from app_factory import create_app
import logging

app = create_app()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
