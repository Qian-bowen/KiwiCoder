# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kiwi/endpoint/protos/kiwi.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fkiwi/endpoint/protos/kiwi.proto\x12\x08\x65ndpoint\"\x11\n\x0fWatchBioRequest\"9\n\x07\x42ioMeta\x12\x0e\n\x06\x62io_id\x18\x01 \x01(\x03\x12\x10\n\x08\x62io_type\x18\x02 \x01(\x03\x12\x0c\n\x04spec\x18\x03 \x01(\t\"E\n\tBioStatus\x12\x0e\n\x06status\x18\x01 \x01(\x03\x12(\n\rbio_meta_list\x18\x02 \x03(\x0b\x32\x11.endpoint.BioMeta\"\x16\n\x14WatchProtocolRequest\" \n\x0eProtocolStatus\x12\x0e\n\x06status\x18\x01 \x01(\x03\"\x1a\n\x18WatchNotificationRequest\"F\n\x14NotificationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x03\x12\x11\n\tmsg_level\x18\x02 \x01(\x03\x12\x0b\n\x03msg\x18\x03 \x01(\t2\xfc\x01\n\x0bKiwiService\x12\x41\n\x0bWatchBioObj\x12\x19.endpoint.WatchBioRequest\x1a\x13.endpoint.BioStatus\"\x00\x30\x01\x12M\n\rWatchProtocol\x12\x1e.endpoint.WatchProtocolRequest\x1a\x18.endpoint.ProtocolStatus\"\x00\x30\x01\x12[\n\x11WatchNotification\x12\".endpoint.WatchNotificationRequest\x1a\x1e.endpoint.NotificationResponse\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kiwi.endpoint.protos.kiwi_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WATCHBIOREQUEST._serialized_start=45
  _WATCHBIOREQUEST._serialized_end=62
  _BIOMETA._serialized_start=64
  _BIOMETA._serialized_end=121
  _BIOSTATUS._serialized_start=123
  _BIOSTATUS._serialized_end=192
  _WATCHPROTOCOLREQUEST._serialized_start=194
  _WATCHPROTOCOLREQUEST._serialized_end=216
  _PROTOCOLSTATUS._serialized_start=218
  _PROTOCOLSTATUS._serialized_end=250
  _WATCHNOTIFICATIONREQUEST._serialized_start=252
  _WATCHNOTIFICATIONREQUEST._serialized_end=278
  _NOTIFICATIONRESPONSE._serialized_start=280
  _NOTIFICATIONRESPONSE._serialized_end=350
  _KIWISERVICE._serialized_start=353
  _KIWISERVICE._serialized_end=605
# @@protoc_insertion_point(module_scope)
