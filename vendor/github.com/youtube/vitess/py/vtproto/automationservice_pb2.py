# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: automationservice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import automation_pb2 as automation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='automationservice.proto',
  package='automationservice',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x61utomationservice.proto\x12\x11\x61utomationservice\x1a\x10\x61utomation.proto2\x81\x02\n\nAutomation\x12t\n\x17\x45nqueueClusterOperation\x12*.automation.EnqueueClusterOperationRequest\x1a+.automation.EnqueueClusterOperationResponse\"\x00\x12}\n\x1aGetClusterOperationDetails\x12-.automation.GetClusterOperationDetailsRequest\x1a..automation.GetClusterOperationDetailsResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[automation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class AutomationStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.EnqueueClusterOperation = channel.unary_unary(
        '/automationservice.Automation/EnqueueClusterOperation',
        request_serializer=automation__pb2.EnqueueClusterOperationRequest.SerializeToString,
        response_deserializer=automation__pb2.EnqueueClusterOperationResponse.FromString,
        )
    self.GetClusterOperationDetails = channel.unary_unary(
        '/automationservice.Automation/GetClusterOperationDetails',
        request_serializer=automation__pb2.GetClusterOperationDetailsRequest.SerializeToString,
        response_deserializer=automation__pb2.GetClusterOperationDetailsResponse.FromString,
        )


class AutomationServicer(object):

  def EnqueueClusterOperation(self, request, context):
    """Start a cluster operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetClusterOperationDetails(self, request, context):
    """TODO(mberlin): Polling this is bad. Implement a subscribe mechanism to wait for changes?
    Get all details of an active cluster operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AutomationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'EnqueueClusterOperation': grpc.unary_unary_rpc_method_handler(
          servicer.EnqueueClusterOperation,
          request_deserializer=automation__pb2.EnqueueClusterOperationRequest.FromString,
          response_serializer=automation__pb2.EnqueueClusterOperationResponse.SerializeToString,
      ),
      'GetClusterOperationDetails': grpc.unary_unary_rpc_method_handler(
          servicer.GetClusterOperationDetails,
          request_deserializer=automation__pb2.GetClusterOperationDetailsRequest.FromString,
          response_serializer=automation__pb2.GetClusterOperationDetailsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'automationservice.Automation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaAutomationServicer(object):
  def EnqueueClusterOperation(self, request, context):
    """Start a cluster operation.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetClusterOperationDetails(self, request, context):
    """TODO(mberlin): Polling this is bad. Implement a subscribe mechanism to wait for changes?
    Get all details of an active cluster operation.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaAutomationStub(object):
  def EnqueueClusterOperation(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Start a cluster operation.
    """
    raise NotImplementedError()
  EnqueueClusterOperation.future = None
  def GetClusterOperationDetails(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """TODO(mberlin): Polling this is bad. Implement a subscribe mechanism to wait for changes?
    Get all details of an active cluster operation.
    """
    raise NotImplementedError()
  GetClusterOperationDetails.future = None


def beta_create_Automation_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('automationservice.Automation', 'EnqueueClusterOperation'): automation__pb2.EnqueueClusterOperationRequest.FromString,
    ('automationservice.Automation', 'GetClusterOperationDetails'): automation__pb2.GetClusterOperationDetailsRequest.FromString,
  }
  response_serializers = {
    ('automationservice.Automation', 'EnqueueClusterOperation'): automation__pb2.EnqueueClusterOperationResponse.SerializeToString,
    ('automationservice.Automation', 'GetClusterOperationDetails'): automation__pb2.GetClusterOperationDetailsResponse.SerializeToString,
  }
  method_implementations = {
    ('automationservice.Automation', 'EnqueueClusterOperation'): face_utilities.unary_unary_inline(servicer.EnqueueClusterOperation),
    ('automationservice.Automation', 'GetClusterOperationDetails'): face_utilities.unary_unary_inline(servicer.GetClusterOperationDetails),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Automation_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('automationservice.Automation', 'EnqueueClusterOperation'): automation__pb2.EnqueueClusterOperationRequest.SerializeToString,
    ('automationservice.Automation', 'GetClusterOperationDetails'): automation__pb2.GetClusterOperationDetailsRequest.SerializeToString,
  }
  response_deserializers = {
    ('automationservice.Automation', 'EnqueueClusterOperation'): automation__pb2.EnqueueClusterOperationResponse.FromString,
    ('automationservice.Automation', 'GetClusterOperationDetails'): automation__pb2.GetClusterOperationDetailsResponse.FromString,
  }
  cardinalities = {
    'EnqueueClusterOperation': cardinality.Cardinality.UNARY_UNARY,
    'GetClusterOperationDetails': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'automationservice.Automation', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
