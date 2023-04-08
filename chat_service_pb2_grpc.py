# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_service_pb2 as chat__service__pb2


class ChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestHeartbeat = channel.unary_unary(
                '/chat.ChatService/RequestHeartbeat',
                request_serializer=chat__service__pb2.Empty.SerializeToString,
                response_deserializer=chat__service__pb2.HeartbeatResponse.FromString,
                )
        self.ProposeCommit = channel.unary_unary(
                '/chat.ChatService/ProposeCommit',
                request_serializer=chat__service__pb2.CommitRequest.SerializeToString,
                response_deserializer=chat__service__pb2.CommitVote.FromString,
                )
        self.VoteResult = channel.unary_unary(
                '/chat.ChatService/VoteResult',
                request_serializer=chat__service__pb2.CommitVote.SerializeToString,
                response_deserializer=chat__service__pb2.Empty.FromString,
                )


class ChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RequestHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProposeCommit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestHeartbeat,
                    request_deserializer=chat__service__pb2.Empty.FromString,
                    response_serializer=chat__service__pb2.HeartbeatResponse.SerializeToString,
            ),
            'ProposeCommit': grpc.unary_unary_rpc_method_handler(
                    servicer.ProposeCommit,
                    request_deserializer=chat__service__pb2.CommitRequest.FromString,
                    response_serializer=chat__service__pb2.CommitVote.SerializeToString,
            ),
            'VoteResult': grpc.unary_unary_rpc_method_handler(
                    servicer.VoteResult,
                    request_deserializer=chat__service__pb2.CommitVote.FromString,
                    response_serializer=chat__service__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RequestHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.ChatService/RequestHeartbeat',
            chat__service__pb2.Empty.SerializeToString,
            chat__service__pb2.HeartbeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProposeCommit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.ChatService/ProposeCommit',
            chat__service__pb2.CommitRequest.SerializeToString,
            chat__service__pb2.CommitVote.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.ChatService/VoteResult',
            chat__service__pb2.CommitVote.SerializeToString,
            chat__service__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
