import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('songs')
    #     try (){
    #   result = spotify.getTopuser("chebru")



    # }
    # catch(ex){
    #         return error;
    # }
    return func.HttpResponse(
            "Created",
            status_code=201
    )
