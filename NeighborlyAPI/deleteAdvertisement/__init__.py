import azure.functions as func
import uow as unit


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            uow = unit.MongoUnitOfWork()
            collection_name = "advertizements"
            result = uow.delete_by_id(collection_name, id)
            return func.HttpResponse("Deleted successfully an advertisement")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
