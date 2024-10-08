# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpi-motor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0frpi-motor.proto\x12\x0comnirobotrpi\"m\n\x0cStateRequest\x12\r\n\x05vel_x\x18\x01 \x01(\x01\x12\r\n\x05vel_y\x18\x02 \x01(\x01\x12\x0f\n\x07vel_yaw\x18\x03 \x01(\x01\x12\x11\n\tvel_heave\x18\x04 \x01(\x01\x12\r\n\x05pitch\x18\x05 \x01(\x01\x12\x0c\n\x04leds\x18\x06 \x01(\x01\"\x19\n\nStateReply\x12\x0b\n\x03res\x18\x01 \x01(\x08\x32N\n\x08RPIMotor\x12\x42\n\x08SetState\x12\x1a.omnirobotrpi.StateRequest\x1a\x18.omnirobotrpi.StateReply\"\x00\x62\x06proto3')



_STATEREQUEST = DESCRIPTOR.message_types_by_name['StateRequest']
_STATEREPLY = DESCRIPTOR.message_types_by_name['StateReply']
StateRequest = _reflection.GeneratedProtocolMessageType('StateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATEREQUEST,
  '__module__' : 'rpi_motor_pb2'
  # @@protoc_insertion_point(class_scope:omnirobotrpi.StateRequest)
  })
_sym_db.RegisterMessage(StateRequest)

StateReply = _reflection.GeneratedProtocolMessageType('StateReply', (_message.Message,), {
  'DESCRIPTOR' : _STATEREPLY,
  '__module__' : 'rpi_motor_pb2'
  # @@protoc_insertion_point(class_scope:omnirobotrpi.StateReply)
  })
_sym_db.RegisterMessage(StateReply)

_RPIMOTOR = DESCRIPTOR.services_by_name['RPIMotor']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATEREQUEST._serialized_start=33
  _STATEREQUEST._serialized_end=142
  _STATEREPLY._serialized_start=144
  _STATEREPLY._serialized_end=169
  _RPIMOTOR._serialized_start=171
  _RPIMOTOR._serialized_end=249
# @@protoc_insertion_point(module_scope)
