# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import offboard_pb2 as offboard__pb2


class OffboardServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Start = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/Start',
        request_serializer=offboard__pb2.StartRequest.SerializeToString,
        response_deserializer=offboard__pb2.StartResponse.FromString,
        )
    self.Stop = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/Stop',
        request_serializer=offboard__pb2.StopRequest.SerializeToString,
        response_deserializer=offboard__pb2.StopResponse.FromString,
        )
    self.IsActive = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/IsActive',
        request_serializer=offboard__pb2.IsActiveRequest.SerializeToString,
        response_deserializer=offboard__pb2.IsActiveResponse.FromString,
        )
    self.SetAttitude = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/SetAttitude',
        request_serializer=offboard__pb2.SetAttitudeRequest.SerializeToString,
        response_deserializer=offboard__pb2.SetAttitudeResponse.FromString,
        )
    self.SetAttitudeRate = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/SetAttitudeRate',
        request_serializer=offboard__pb2.SetAttitudeRateRequest.SerializeToString,
        response_deserializer=offboard__pb2.SetAttitudeRateResponse.FromString,
        )
    self.SetPositionNed = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/SetPositionNed',
        request_serializer=offboard__pb2.SetPositionNedRequest.SerializeToString,
        response_deserializer=offboard__pb2.SetPositionNedResponse.FromString,
        )
    self.SetVelocityBody = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/SetVelocityBody',
        request_serializer=offboard__pb2.SetVelocityBodyRequest.SerializeToString,
        response_deserializer=offboard__pb2.SetVelocityBodyResponse.FromString,
        )
    self.SetVelocityNed = channel.unary_unary(
        '/dronecode_sdk.rpc.offboard.OffboardService/SetVelocityNed',
        request_serializer=offboard__pb2.SetVelocityNedRequest.SerializeToString,
        response_deserializer=offboard__pb2.SetVelocityNedResponse.FromString,
        )


class OffboardServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Start(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsActive(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetAttitude(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetAttitudeRate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPositionNed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetVelocityBody(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetVelocityNed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OffboardServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=offboard__pb2.StartRequest.FromString,
          response_serializer=offboard__pb2.StartResponse.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=offboard__pb2.StopRequest.FromString,
          response_serializer=offboard__pb2.StopResponse.SerializeToString,
      ),
      'IsActive': grpc.unary_unary_rpc_method_handler(
          servicer.IsActive,
          request_deserializer=offboard__pb2.IsActiveRequest.FromString,
          response_serializer=offboard__pb2.IsActiveResponse.SerializeToString,
      ),
      'SetAttitude': grpc.unary_unary_rpc_method_handler(
          servicer.SetAttitude,
          request_deserializer=offboard__pb2.SetAttitudeRequest.FromString,
          response_serializer=offboard__pb2.SetAttitudeResponse.SerializeToString,
      ),
      'SetAttitudeRate': grpc.unary_unary_rpc_method_handler(
          servicer.SetAttitudeRate,
          request_deserializer=offboard__pb2.SetAttitudeRateRequest.FromString,
          response_serializer=offboard__pb2.SetAttitudeRateResponse.SerializeToString,
      ),
      'SetPositionNed': grpc.unary_unary_rpc_method_handler(
          servicer.SetPositionNed,
          request_deserializer=offboard__pb2.SetPositionNedRequest.FromString,
          response_serializer=offboard__pb2.SetPositionNedResponse.SerializeToString,
      ),
      'SetVelocityBody': grpc.unary_unary_rpc_method_handler(
          servicer.SetVelocityBody,
          request_deserializer=offboard__pb2.SetVelocityBodyRequest.FromString,
          response_serializer=offboard__pb2.SetVelocityBodyResponse.SerializeToString,
      ),
      'SetVelocityNed': grpc.unary_unary_rpc_method_handler(
          servicer.SetVelocityNed,
          request_deserializer=offboard__pb2.SetVelocityNedRequest.FromString,
          response_serializer=offboard__pb2.SetVelocityNedResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dronecode_sdk.rpc.offboard.OffboardService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
