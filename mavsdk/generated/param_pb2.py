# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='param.proto',
  package='dronecode_sdk.rpc.param',
  syntax='proto3',
  serialized_options=_b('\n\026io.dronecode_sdk.paramB\nParamProto'),
  serialized_pb=_b('\n\x0bparam.proto\x12\x17\x64ronecode_sdk.rpc.param\"\"\n\x12GetIntParamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"`\n\x13GetIntParamResponse\x12:\n\x0cparam_result\x18\x01 \x01(\x0b\x32$.dronecode_sdk.rpc.param.ParamResult\x12\r\n\x05value\x18\x02 \x01(\x05\"1\n\x12SetIntParamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"Q\n\x13SetIntParamResponse\x12:\n\x0cparam_result\x18\x01 \x01(\x0b\x32$.dronecode_sdk.rpc.param.ParamResult\"$\n\x14GetFloatParamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"b\n\x15GetFloatParamResponse\x12:\n\x0cparam_result\x18\x01 \x01(\x0b\x32$.dronecode_sdk.rpc.param.ParamResult\x12\r\n\x05value\x18\x02 \x01(\x02\"3\n\x14SetFloatParamRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"S\n\x15SetFloatParamResponse\x12:\n\x0cparam_result\x18\x01 \x01(\x0b\x32$.dronecode_sdk.rpc.param.ParamResult\"\xce\x01\n\x0bParamResult\x12;\n\x06result\x18\x01 \x01(\x0e\x32+.dronecode_sdk.rpc.param.ParamResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"n\n\x06Result\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02\x12\x14\n\x10\x43ONNECTION_ERROR\x10\x03\x12\x0e\n\nWRONG_TYPE\x10\x04\x12\x17\n\x13PARAM_NAME_TOO_LONG\x10\x05\x32\xca\x03\n\x0cParamService\x12j\n\x0bGetIntParam\x12+.dronecode_sdk.rpc.param.GetIntParamRequest\x1a,.dronecode_sdk.rpc.param.GetIntParamResponse\"\x00\x12j\n\x0bSetIntParam\x12+.dronecode_sdk.rpc.param.SetIntParamRequest\x1a,.dronecode_sdk.rpc.param.SetIntParamResponse\"\x00\x12p\n\rGetFloatParam\x12-.dronecode_sdk.rpc.param.GetFloatParamRequest\x1a..dronecode_sdk.rpc.param.GetFloatParamResponse\"\x00\x12p\n\rSetFloatParam\x12-.dronecode_sdk.rpc.param.SetFloatParamRequest\x1a..dronecode_sdk.rpc.param.SetFloatParamResponse\"\x00\x42$\n\x16io.dronecode_sdk.paramB\nParamProtob\x06proto3')
)



_PARAMRESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='dronecode_sdk.rpc.param.ParamResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_TYPE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAM_NAME_TOO_LONG', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=681,
  serialized_end=791,
)
_sym_db.RegisterEnumDescriptor(_PARAMRESULT_RESULT)


_GETINTPARAMREQUEST = _descriptor.Descriptor(
  name='GetIntParamRequest',
  full_name='dronecode_sdk.rpc.param.GetIntParamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dronecode_sdk.rpc.param.GetIntParamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=40,
  serialized_end=74,
)


_GETINTPARAMRESPONSE = _descriptor.Descriptor(
  name='GetIntParamResponse',
  full_name='dronecode_sdk.rpc.param.GetIntParamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_result', full_name='dronecode_sdk.rpc.param.GetIntParamResponse.param_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dronecode_sdk.rpc.param.GetIntParamResponse.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=76,
  serialized_end=172,
)


_SETINTPARAMREQUEST = _descriptor.Descriptor(
  name='SetIntParamRequest',
  full_name='dronecode_sdk.rpc.param.SetIntParamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dronecode_sdk.rpc.param.SetIntParamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dronecode_sdk.rpc.param.SetIntParamRequest.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=174,
  serialized_end=223,
)


_SETINTPARAMRESPONSE = _descriptor.Descriptor(
  name='SetIntParamResponse',
  full_name='dronecode_sdk.rpc.param.SetIntParamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_result', full_name='dronecode_sdk.rpc.param.SetIntParamResponse.param_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=225,
  serialized_end=306,
)


_GETFLOATPARAMREQUEST = _descriptor.Descriptor(
  name='GetFloatParamRequest',
  full_name='dronecode_sdk.rpc.param.GetFloatParamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dronecode_sdk.rpc.param.GetFloatParamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=308,
  serialized_end=344,
)


_GETFLOATPARAMRESPONSE = _descriptor.Descriptor(
  name='GetFloatParamResponse',
  full_name='dronecode_sdk.rpc.param.GetFloatParamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_result', full_name='dronecode_sdk.rpc.param.GetFloatParamResponse.param_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dronecode_sdk.rpc.param.GetFloatParamResponse.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=444,
)


_SETFLOATPARAMREQUEST = _descriptor.Descriptor(
  name='SetFloatParamRequest',
  full_name='dronecode_sdk.rpc.param.SetFloatParamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dronecode_sdk.rpc.param.SetFloatParamRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dronecode_sdk.rpc.param.SetFloatParamRequest.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=446,
  serialized_end=497,
)


_SETFLOATPARAMRESPONSE = _descriptor.Descriptor(
  name='SetFloatParamResponse',
  full_name='dronecode_sdk.rpc.param.SetFloatParamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_result', full_name='dronecode_sdk.rpc.param.SetFloatParamResponse.param_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=499,
  serialized_end=582,
)


_PARAMRESULT = _descriptor.Descriptor(
  name='ParamResult',
  full_name='dronecode_sdk.rpc.param.ParamResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='dronecode_sdk.rpc.param.ParamResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='dronecode_sdk.rpc.param.ParamResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARAMRESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=791,
)

_GETINTPARAMRESPONSE.fields_by_name['param_result'].message_type = _PARAMRESULT
_SETINTPARAMRESPONSE.fields_by_name['param_result'].message_type = _PARAMRESULT
_GETFLOATPARAMRESPONSE.fields_by_name['param_result'].message_type = _PARAMRESULT
_SETFLOATPARAMRESPONSE.fields_by_name['param_result'].message_type = _PARAMRESULT
_PARAMRESULT.fields_by_name['result'].enum_type = _PARAMRESULT_RESULT
_PARAMRESULT_RESULT.containing_type = _PARAMRESULT
DESCRIPTOR.message_types_by_name['GetIntParamRequest'] = _GETINTPARAMREQUEST
DESCRIPTOR.message_types_by_name['GetIntParamResponse'] = _GETINTPARAMRESPONSE
DESCRIPTOR.message_types_by_name['SetIntParamRequest'] = _SETINTPARAMREQUEST
DESCRIPTOR.message_types_by_name['SetIntParamResponse'] = _SETINTPARAMRESPONSE
DESCRIPTOR.message_types_by_name['GetFloatParamRequest'] = _GETFLOATPARAMREQUEST
DESCRIPTOR.message_types_by_name['GetFloatParamResponse'] = _GETFLOATPARAMRESPONSE
DESCRIPTOR.message_types_by_name['SetFloatParamRequest'] = _SETFLOATPARAMREQUEST
DESCRIPTOR.message_types_by_name['SetFloatParamResponse'] = _SETFLOATPARAMRESPONSE
DESCRIPTOR.message_types_by_name['ParamResult'] = _PARAMRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetIntParamRequest = _reflection.GeneratedProtocolMessageType('GetIntParamRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINTPARAMREQUEST,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.GetIntParamRequest)
  ))
_sym_db.RegisterMessage(GetIntParamRequest)

GetIntParamResponse = _reflection.GeneratedProtocolMessageType('GetIntParamResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINTPARAMRESPONSE,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.GetIntParamResponse)
  ))
_sym_db.RegisterMessage(GetIntParamResponse)

SetIntParamRequest = _reflection.GeneratedProtocolMessageType('SetIntParamRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETINTPARAMREQUEST,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.SetIntParamRequest)
  ))
_sym_db.RegisterMessage(SetIntParamRequest)

SetIntParamResponse = _reflection.GeneratedProtocolMessageType('SetIntParamResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETINTPARAMRESPONSE,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.SetIntParamResponse)
  ))
_sym_db.RegisterMessage(SetIntParamResponse)

GetFloatParamRequest = _reflection.GeneratedProtocolMessageType('GetFloatParamRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFLOATPARAMREQUEST,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.GetFloatParamRequest)
  ))
_sym_db.RegisterMessage(GetFloatParamRequest)

GetFloatParamResponse = _reflection.GeneratedProtocolMessageType('GetFloatParamResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFLOATPARAMRESPONSE,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.GetFloatParamResponse)
  ))
_sym_db.RegisterMessage(GetFloatParamResponse)

SetFloatParamRequest = _reflection.GeneratedProtocolMessageType('SetFloatParamRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETFLOATPARAMREQUEST,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.SetFloatParamRequest)
  ))
_sym_db.RegisterMessage(SetFloatParamRequest)

SetFloatParamResponse = _reflection.GeneratedProtocolMessageType('SetFloatParamResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETFLOATPARAMRESPONSE,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.SetFloatParamResponse)
  ))
_sym_db.RegisterMessage(SetFloatParamResponse)

ParamResult = _reflection.GeneratedProtocolMessageType('ParamResult', (_message.Message,), dict(
  DESCRIPTOR = _PARAMRESULT,
  __module__ = 'param_pb2'
  # @@protoc_insertion_point(class_scope:dronecode_sdk.rpc.param.ParamResult)
  ))
_sym_db.RegisterMessage(ParamResult)


DESCRIPTOR._options = None

_PARAMSERVICE = _descriptor.ServiceDescriptor(
  name='ParamService',
  full_name='dronecode_sdk.rpc.param.ParamService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=794,
  serialized_end=1252,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetIntParam',
    full_name='dronecode_sdk.rpc.param.ParamService.GetIntParam',
    index=0,
    containing_service=None,
    input_type=_GETINTPARAMREQUEST,
    output_type=_GETINTPARAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetIntParam',
    full_name='dronecode_sdk.rpc.param.ParamService.SetIntParam',
    index=1,
    containing_service=None,
    input_type=_SETINTPARAMREQUEST,
    output_type=_SETINTPARAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFloatParam',
    full_name='dronecode_sdk.rpc.param.ParamService.GetFloatParam',
    index=2,
    containing_service=None,
    input_type=_GETFLOATPARAMREQUEST,
    output_type=_GETFLOATPARAMRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetFloatParam',
    full_name='dronecode_sdk.rpc.param.ParamService.SetFloatParam',
    index=3,
    containing_service=None,
    input_type=_SETFLOATPARAMREQUEST,
    output_type=_SETFLOATPARAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PARAMSERVICE)

DESCRIPTOR.services_by_name['ParamService'] = _PARAMSERVICE

# @@protoc_insertion_point(module_scope)
