# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smile_lowercase.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='smile_lowercase.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15smile_lowercase.proto\"$\n\x11LowerSmileRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\".\n\nLowerSmile\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"6\n\x12LowerSmileResponse\x12 \n\x0bLowerSmiles\x18\x01 \x03(\x0b\x32\x0b.LowerSmile2C\n\nLowrSmiles\x12\x35\n\nlowersmile\x12\x12.LowerSmileRequest\x1a\x13.LowerSmileResponseb\x06proto3'
)




_LOWERSMILEREQUEST = _descriptor.Descriptor(
  name='LowerSmileRequest',
  full_name='LowerSmileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='LowerSmileRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=25,
  serialized_end=61,
)


_LOWERSMILE = _descriptor.Descriptor(
  name='LowerSmile',
  full_name='LowerSmile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='LowerSmile.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='LowerSmile.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=109,
)


_LOWERSMILERESPONSE = _descriptor.Descriptor(
  name='LowerSmileResponse',
  full_name='LowerSmileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='LowerSmiles', full_name='LowerSmileResponse.LowerSmiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=111,
  serialized_end=165,
)

_LOWERSMILERESPONSE.fields_by_name['LowerSmiles'].message_type = _LOWERSMILE
DESCRIPTOR.message_types_by_name['LowerSmileRequest'] = _LOWERSMILEREQUEST
DESCRIPTOR.message_types_by_name['LowerSmile'] = _LOWERSMILE
DESCRIPTOR.message_types_by_name['LowerSmileResponse'] = _LOWERSMILERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LowerSmileRequest = _reflection.GeneratedProtocolMessageType('LowerSmileRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOWERSMILEREQUEST,
  '__module__' : 'smile_lowercase_pb2'
  # @@protoc_insertion_point(class_scope:LowerSmileRequest)
  })
_sym_db.RegisterMessage(LowerSmileRequest)

LowerSmile = _reflection.GeneratedProtocolMessageType('LowerSmile', (_message.Message,), {
  'DESCRIPTOR' : _LOWERSMILE,
  '__module__' : 'smile_lowercase_pb2'
  # @@protoc_insertion_point(class_scope:LowerSmile)
  })
_sym_db.RegisterMessage(LowerSmile)

LowerSmileResponse = _reflection.GeneratedProtocolMessageType('LowerSmileResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOWERSMILERESPONSE,
  '__module__' : 'smile_lowercase_pb2'
  # @@protoc_insertion_point(class_scope:LowerSmileResponse)
  })
_sym_db.RegisterMessage(LowerSmileResponse)



_LOWRSMILES = _descriptor.ServiceDescriptor(
  name='LowrSmiles',
  full_name='LowrSmiles',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=167,
  serialized_end=234,
  methods=[
  _descriptor.MethodDescriptor(
    name='lowersmile',
    full_name='LowrSmiles.lowersmile',
    index=0,
    containing_service=None,
    input_type=_LOWERSMILEREQUEST,
    output_type=_LOWERSMILERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOWRSMILES)

DESCRIPTOR.services_by_name['LowrSmiles'] = _LOWRSMILES

# @@protoc_insertion_point(module_scope)