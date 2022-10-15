import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema, StoreUpdateSchema

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, message="Store not found.")

    @blp.response(200, StoreSchema)
    def delete(self, store_id):
        try:
            store = stores[store_id]
            del stores[store_id]
            return store
        except KeyError:
            abort(404, message="Store not found.")

    @blp.response(200, StoreSchema)
    @blp.arguments(StoreUpdateSchema)
    def put(self, store_data, store_id):
        try:
            store = stores[store_id]
            store |= store_data
            return store
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")
class Stores(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.response(201, StoreSchema)
    @blp.arguments(StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store["name"] == store_data["name"]:
                abort(400, message="Store already exists")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store
