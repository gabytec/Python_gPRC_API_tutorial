# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='unary.proto',
  package='unary',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bunary.proto\x12\x05unary\"a\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x16\n\x0e\x66irst_sentence\x18\x04 \x01(\t\x12\x16\n\x0eyear_published\x18\x05 \x01(\t\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\nMessagePut\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\",\n\x0bMessagePost\x12\x1d\n\x08\x62ookPost\x18\x01 \x01(\x0b\x32\x0b.unary.Book\"4\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\")\n\x0c\x42ookResponse\x12\x19\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x0b.unary.Book\"+\n\rBooksResponse\x12\x1a\n\x05\x62ooks\x18\x01 \x01(\x0b\x32\x0b.unary.Book2\xd1\x02\n\x05Unary\x12=\n\x11GetServerResponse\x12\x0e.unary.Message\x1a\x16.unary.MessageResponse\"\x00\x12\x34\n\x08GetBooks\x12\x0e.unary.Message\x1a\x14.unary.BooksResponse\"\x00\x30\x01\x12\x30\n\x07GetBook\x12\x0e.unary.Message\x1a\x13.unary.BookResponse\"\x00\x12\x36\n\nDeleteBook\x12\x0e.unary.Message\x1a\x16.unary.MessageResponse\"\x00\x12\x36\n\x07PutBook\x12\x11.unary.MessagePut\x1a\x16.unary.MessageResponse\"\x00\x12\x31\n\x08PostBook\x12\x0b.unary.Book\x1a\x16.unary.MessageResponse\"\x00\x62\x06proto3'
)




_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='unary.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='unary.Book.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='unary.Book.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='unary.Book.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_sentence', full_name='unary.Book.first_sentence', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year_published', full_name='unary.Book.year_published', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=119,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='unary.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='unary.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=147,
)


_MESSAGEPUT = _descriptor.Descriptor(
  name='MessagePut',
  full_name='unary.MessagePut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='unary.MessagePut.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='unary.MessagePut.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='unary.MessagePut.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=201,
)


_MESSAGEPOST = _descriptor.Descriptor(
  name='MessagePost',
  full_name='unary.MessagePost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookPost', full_name='unary.MessagePost.bookPost', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=247,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='unary.MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='unary.MessageResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='received', full_name='unary.MessageResponse.received', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=301,
)


_BOOKRESPONSE = _descriptor.Descriptor(
  name='BookResponse',
  full_name='unary.BookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='unary.BookResponse.book', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=344,
)


_BOOKSRESPONSE = _descriptor.Descriptor(
  name='BooksResponse',
  full_name='unary.BooksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='unary.BooksResponse.books', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=389,
)

_MESSAGEPOST.fields_by_name['bookPost'].message_type = _BOOK
_BOOKRESPONSE.fields_by_name['book'].message_type = _BOOK
_BOOKSRESPONSE.fields_by_name['books'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessagePut'] = _MESSAGEPUT
DESCRIPTOR.message_types_by_name['MessagePost'] = _MESSAGEPOST
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
DESCRIPTOR.message_types_by_name['BookResponse'] = _BOOKRESPONSE
DESCRIPTOR.message_types_by_name['BooksResponse'] = _BOOKSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.Book)
  })
_sym_db.RegisterMessage(Book)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.Message)
  })
_sym_db.RegisterMessage(Message)

MessagePut = _reflection.GeneratedProtocolMessageType('MessagePut', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPUT,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.MessagePut)
  })
_sym_db.RegisterMessage(MessagePut)

MessagePost = _reflection.GeneratedProtocolMessageType('MessagePost', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPOST,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.MessagePost)
  })
_sym_db.RegisterMessage(MessagePost)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)

BookResponse = _reflection.GeneratedProtocolMessageType('BookResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRESPONSE,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.BookResponse)
  })
_sym_db.RegisterMessage(BookResponse)

BooksResponse = _reflection.GeneratedProtocolMessageType('BooksResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKSRESPONSE,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.BooksResponse)
  })
_sym_db.RegisterMessage(BooksResponse)



_UNARY = _descriptor.ServiceDescriptor(
  name='Unary',
  full_name='unary.Unary',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=392,
  serialized_end=729,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='unary.Unary.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBooks',
    full_name='unary.Unary.GetBooks',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_BOOKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='unary.Unary.GetBook',
    index=2,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_BOOKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBook',
    full_name='unary.Unary.DeleteBook',
    index=3,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PutBook',
    full_name='unary.Unary.PutBook',
    index=4,
    containing_service=None,
    input_type=_MESSAGEPUT,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostBook',
    full_name='unary.Unary.PostBook',
    index=5,
    containing_service=None,
    input_type=_BOOK,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_UNARY)

DESCRIPTOR.services_by_name['Unary'] = _UNARY

# @@protoc_insertion_point(module_scope)
