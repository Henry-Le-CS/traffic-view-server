from .predict_route import predict_blueprint

def register_route(app):
    app.register_blueprint(predict_blueprint)