from concurrent import futures
import grpc
import time
import logging
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import unary_resources

class UnaryService(pb2_grpc.UnaryServicer):
    def __init__(self):
        self.db = unary_resources.read_database()

    def GetServerResponse(self, request, context):
        message = request.message
        result2 = 'Hello I am up and running received ' +message + ' message from you'
        result = {'message': result2, 'received': True}
        return pb2.MessageResponse(**result)

    
    def GetBooks(self, request, context):
        message = request.message
        i = 0
        leng = len(self.db)
        if(leng == 0):
            message = pb2.Book(id= "", title= "", author= "", first_sentence= "",
            year_published= "")
            result = {'books': message}
            yield pb2.BooksResponse(**result)
        else:
            while (i < leng):
                result = {'books': self.db[i]}
                i = i + 1 
                yield pb2.BooksResponse(**result)
    
    def GetBook(self, request, context):
        message = request.message
        print(message)
        #result = {'book': self.db[0]}
        #return pb2.BookResponse(**result)
        i = 0
        leng = len(self.db)
        if(leng == 0):
            message = pb2.Book(id= "", title= "", author= "", first_sentence= "",
            year_published= "")
            result = {'books': message}
            return pb2.BooksResponse(**result)
        else:
            flag = False
            while (i < leng):
                if(message == str(self.db[i].id)):
                    flag = True
                    break
                else:
                    i = i + 1
            if(flag == True):
                result = {'book': self.db[i]}
                return pb2.BookResponse(**result)
            else:   
                message = pb2.Book(id= "", title= "", author= "", first_sentence= "",
                year_published= "")
                result = {'books': message}
                return pb2.BooksResponse(**result)

    def DeleteBook(self, request, context):
        message = request.message
        i = 0
        leng = len(self.db)
        if(leng == 0):
            result = {'message': "fail", 'received': True}
            return pb2.MessageResponse(**result)
        else:
            flag = False
            while (i < leng):
                if(message == str(self.db[i].id)):
                    flag = True
                    self.db.pop(i)
                    break
                else:
                    i = i + 1
            if(flag == True):
                result = {'message': "ok", 'received': True}
                return pb2.MessageResponse(**result)
            else:   
                result = {'message': "fail", 'received': True}
                return pb2.MessageResponse(**result)
    
    def PutBook(self, request, context):
        idBook = request.id
        keyBook = request.key
        valueBook = request.value
        i = 0
        leng = len(self.db)
        if(leng == 0):
            result = {'message': "fail", 'received': True}
            return pb2.MessageResponse(**result)
        else:
            flag = False
            while (i < leng):
                if(idBook == str(self.db[i].id)):
                    if(keyBook == "title"):
                        self.db[i].title = valueBook
                    elif(keyBook == "author"):
                        self.db[i].author = valueBook
                    elif(keyBook == "first_sentence"):
                        self.db[i].first_sentence = valueBook
                    elif(keyBook == "year_published"):
                        self.db[i].year_published = valueBook
                    flag = True
                    break
                else:
                    i = i + 1
            if(flag == True):
                result = {'message': "ok", 'received': True}
                return pb2.MessageResponse(**result)
            else:   
                result = {'message': "fail", 'received': True}
                return pb2.MessageResponse(**result)
    
    def PostBook(self, request, context):
        message = request
        leng = len(self.db)
        flag = False
        i = 0
        print(request.id)
        while (i < leng):
            if(request.id == str(self.db[i].id)):
                flag = True
                break
            else:
                i = i + 1
        if(flag == True):
            result = {'message': "fail", 'received': True}
            return pb2.MessageResponse(**result)
        else:
            self.db.append(message)
            result = {'message': "ok", 'received': True}
            return pb2.MessageResponse(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()