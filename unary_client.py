from __future__ import print_function
import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2
import logging

def get_message(stub):
    message="0"
    message = pb2.Message(message=message)
    result = stub.GetServerResponse(message)
    print(result)


def get_book(stub, value):
    message = value
    message = pb2.Message(message=message)
    result = stub.GetBook(message)
    print(result)

def get_books(stub):
    message="all"
    message = pb2.Message(message=message)
    result = stub.GetBooks(message)
    for x in result:
        print(x)

def delete_book(stub, value):
    message = value
    message = pb2.Message(message=message)
    result = stub.DeleteBook(message)
    print(result)

def put_book(stub, id, key, value):
    #id = "0"
    #key = 'title'
    #value = 'el principito'
    message = pb2.MessagePut(id=id, key=key, value=value)
    result = stub.PutBook(message)
    print(result)

def post_book(stub, idB, title, author, first_sentence, year_published):
    message = pb2.Book(id = idB, title = title, author = author, first_sentence = first_sentence,
    year_published = year_published)
    result = stub.PostBook(message)
    print(result)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.UnaryStub(channel)
        get_message(stub)
        print("-------------- GetBook --------------")
        get_book(stub, "1")
        print("-------------- GetBooks --------------")
        get_books(stub)
        print("-------------- DeleteBook --------------")
        delete_book(stub, "0")
        print("-------------- GetBooks --------------")
        get_book(stub, "0")
        print("-------------- PutBook --------------")
        put_book(stub, '0', 'title', 'el principito')
        print("-------------- GetBooks --------------")
        get_books(stub)
        print("-------------- PostBook --------------")
        post_book(stub, "2", "The Silmarillion", "J.R.R Tolkien", "there was Eru the One.", "1999")
        print("-------------- GetBooks --------------")
        get_books(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()