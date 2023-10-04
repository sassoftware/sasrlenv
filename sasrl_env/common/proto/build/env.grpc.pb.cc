// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: env.proto

#include "env.pb.h"
#include "env.grpc.pb.h"

#include <functional>
#include <grpcpp/support/async_stream.h>
#include <grpcpp/support/async_unary_call.h>
#include <grpcpp/impl/channel_interface.h>
#include <grpcpp/impl/client_unary_call.h>
#include <grpcpp/support/client_callback.h>
#include <grpcpp/support/message_allocator.h>
#include <grpcpp/support/method_handler.h>
#include <grpcpp/impl/rpc_service_method.h>
#include <grpcpp/support/server_callback.h>
#include <grpcpp/impl/codegen/server_callback_handlers.h>
#include <grpcpp/server_context.h>
#include <grpcpp/impl/service_type.h>
#include <grpcpp/support/sync_stream.h>

static const char* EnvControl_method_names[] = {
  "/EnvControl/Start",
  "/EnvControl/Close",
};

std::unique_ptr< EnvControl::Stub> EnvControl::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< EnvControl::Stub> stub(new EnvControl::Stub(channel, options));
  return stub;
}

EnvControl::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options)
  : channel_(channel), rpcmethod_Start_(EnvControl_method_names[0], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Close_(EnvControl_method_names[1], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status EnvControl::Stub::Start(::grpc::ClientContext* context, const ::Empty& request, ::ServerInfo* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Empty, ::ServerInfo, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Start_, context, request, response);
}

void EnvControl::Stub::async::Start(::grpc::ClientContext* context, const ::Empty* request, ::ServerInfo* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Empty, ::ServerInfo, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Start_, context, request, response, std::move(f));
}

void EnvControl::Stub::async::Start(::grpc::ClientContext* context, const ::Empty* request, ::ServerInfo* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Start_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::ServerInfo>* EnvControl::Stub::PrepareAsyncStartRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::ServerInfo, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Start_, context, request);
}

::grpc::ClientAsyncResponseReader< ::ServerInfo>* EnvControl::Stub::AsyncStartRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncStartRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status EnvControl::Stub::Close(::grpc::ClientContext* context, const ::ServerInfo& request, ::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::ServerInfo, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Close_, context, request, response);
}

void EnvControl::Stub::async::Close(::grpc::ClientContext* context, const ::ServerInfo* request, ::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::ServerInfo, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Close_, context, request, response, std::move(f));
}

void EnvControl::Stub::async::Close(::grpc::ClientContext* context, const ::ServerInfo* request, ::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Close_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Empty>* EnvControl::Stub::PrepareAsyncCloseRaw(::grpc::ClientContext* context, const ::ServerInfo& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Empty, ::ServerInfo, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Close_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Empty>* EnvControl::Stub::AsyncCloseRaw(::grpc::ClientContext* context, const ::ServerInfo& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncCloseRaw(context, request, cq);
  result->StartCall();
  return result;
}

EnvControl::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      EnvControl_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< EnvControl::Service, ::Empty, ::ServerInfo, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](EnvControl::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Empty* req,
             ::ServerInfo* resp) {
               return service->Start(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      EnvControl_method_names[1],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< EnvControl::Service, ::ServerInfo, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](EnvControl::Service* service,
             ::grpc::ServerContext* ctx,
             const ::ServerInfo* req,
             ::Empty* resp) {
               return service->Close(ctx, req, resp);
             }, this)));
}

EnvControl::Service::~Service() {
}

::grpc::Status EnvControl::Service::Start(::grpc::ServerContext* context, const ::Empty* request, ::ServerInfo* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status EnvControl::Service::Close(::grpc::ServerContext* context, const ::ServerInfo* request, ::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


static const char* Env_method_names[] = {
  "/Env/Handshake",
  "/Env/Make",
  "/Env/Reset",
  "/Env/Step",
  "/Env/Render",
  "/Env/Seed",
  "/Env/Sample",
  "/Env/Close",
};

std::unique_ptr< Env::Stub> Env::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< Env::Stub> stub(new Env::Stub(channel, options));
  return stub;
}

Env::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options)
  : channel_(channel), rpcmethod_Handshake_(Env_method_names[0], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Make_(Env_method_names[1], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Reset_(Env_method_names[2], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Step_(Env_method_names[3], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Render_(Env_method_names[4], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Seed_(Env_method_names[5], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Sample_(Env_method_names[6], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_Close_(Env_method_names[7], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status Env::Stub::Handshake(::grpc::ClientContext* context, const ::Empty& request, ::MetaData* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Empty, ::MetaData, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Handshake_, context, request, response);
}

void Env::Stub::async::Handshake(::grpc::ClientContext* context, const ::Empty* request, ::MetaData* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Empty, ::MetaData, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Handshake_, context, request, response, std::move(f));
}

void Env::Stub::async::Handshake(::grpc::ClientContext* context, const ::Empty* request, ::MetaData* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Handshake_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::MetaData>* Env::Stub::PrepareAsyncHandshakeRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::MetaData, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Handshake_, context, request);
}

::grpc::ClientAsyncResponseReader< ::MetaData>* Env::Stub::AsyncHandshakeRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncHandshakeRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Make(::grpc::ClientContext* context, const ::Name& request, ::Info* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Name, ::Info, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Make_, context, request, response);
}

void Env::Stub::async::Make(::grpc::ClientContext* context, const ::Name* request, ::Info* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Name, ::Info, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Make_, context, request, response, std::move(f));
}

void Env::Stub::async::Make(::grpc::ClientContext* context, const ::Name* request, ::Info* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Make_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Info>* Env::Stub::PrepareAsyncMakeRaw(::grpc::ClientContext* context, const ::Name& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Info, ::Name, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Make_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Info>* Env::Stub::AsyncMakeRaw(::grpc::ClientContext* context, const ::Name& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncMakeRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Reset(::grpc::ClientContext* context, const ::Empty& request, ::Transition* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Empty, ::Transition, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Reset_, context, request, response);
}

void Env::Stub::async::Reset(::grpc::ClientContext* context, const ::Empty* request, ::Transition* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Empty, ::Transition, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Reset_, context, request, response, std::move(f));
}

void Env::Stub::async::Reset(::grpc::ClientContext* context, const ::Empty* request, ::Transition* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Reset_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Transition>* Env::Stub::PrepareAsyncResetRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Transition, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Reset_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Transition>* Env::Stub::AsyncResetRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncResetRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Step(::grpc::ClientContext* context, const ::Action& request, ::Transition* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Action, ::Transition, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Step_, context, request, response);
}

void Env::Stub::async::Step(::grpc::ClientContext* context, const ::Action* request, ::Transition* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Action, ::Transition, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Step_, context, request, response, std::move(f));
}

void Env::Stub::async::Step(::grpc::ClientContext* context, const ::Action* request, ::Transition* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Step_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Transition>* Env::Stub::PrepareAsyncStepRaw(::grpc::ClientContext* context, const ::Action& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Transition, ::Action, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Step_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Transition>* Env::Stub::AsyncStepRaw(::grpc::ClientContext* context, const ::Action& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncStepRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Render(::grpc::ClientContext* context, const ::RenderMode& request, ::RenderOut* response) {
  return ::grpc::internal::BlockingUnaryCall< ::RenderMode, ::RenderOut, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Render_, context, request, response);
}

void Env::Stub::async::Render(::grpc::ClientContext* context, const ::RenderMode* request, ::RenderOut* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::RenderMode, ::RenderOut, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Render_, context, request, response, std::move(f));
}

void Env::Stub::async::Render(::grpc::ClientContext* context, const ::RenderMode* request, ::RenderOut* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Render_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::RenderOut>* Env::Stub::PrepareAsyncRenderRaw(::grpc::ClientContext* context, const ::RenderMode& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::RenderOut, ::RenderMode, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Render_, context, request);
}

::grpc::ClientAsyncResponseReader< ::RenderOut>* Env::Stub::AsyncRenderRaw(::grpc::ClientContext* context, const ::RenderMode& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncRenderRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Seed(::grpc::ClientContext* context, const ::EnvSeed& request, ::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::EnvSeed, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Seed_, context, request, response);
}

void Env::Stub::async::Seed(::grpc::ClientContext* context, const ::EnvSeed* request, ::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::EnvSeed, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Seed_, context, request, response, std::move(f));
}

void Env::Stub::async::Seed(::grpc::ClientContext* context, const ::EnvSeed* request, ::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Seed_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Empty>* Env::Stub::PrepareAsyncSeedRaw(::grpc::ClientContext* context, const ::EnvSeed& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Empty, ::EnvSeed, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Seed_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Empty>* Env::Stub::AsyncSeedRaw(::grpc::ClientContext* context, const ::EnvSeed& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncSeedRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Sample(::grpc::ClientContext* context, const ::Empty& request, ::Action* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Empty, ::Action, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Sample_, context, request, response);
}

void Env::Stub::async::Sample(::grpc::ClientContext* context, const ::Empty* request, ::Action* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Empty, ::Action, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Sample_, context, request, response, std::move(f));
}

void Env::Stub::async::Sample(::grpc::ClientContext* context, const ::Empty* request, ::Action* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Sample_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Action>* Env::Stub::PrepareAsyncSampleRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Action, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Sample_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Action>* Env::Stub::AsyncSampleRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncSampleRaw(context, request, cq);
  result->StartCall();
  return result;
}

::grpc::Status Env::Stub::Close(::grpc::ClientContext* context, const ::Empty& request, ::Empty* response) {
  return ::grpc::internal::BlockingUnaryCall< ::Empty, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_Close_, context, request, response);
}

void Env::Stub::async::Close(::grpc::ClientContext* context, const ::Empty* request, ::Empty* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::Empty, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Close_, context, request, response, std::move(f));
}

void Env::Stub::async::Close(::grpc::ClientContext* context, const ::Empty* request, ::Empty* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_Close_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::Empty>* Env::Stub::PrepareAsyncCloseRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::Empty, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_Close_, context, request);
}

::grpc::ClientAsyncResponseReader< ::Empty>* Env::Stub::AsyncCloseRaw(::grpc::ClientContext* context, const ::Empty& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncCloseRaw(context, request, cq);
  result->StartCall();
  return result;
}

Env::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::Empty, ::MetaData, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Empty* req,
             ::MetaData* resp) {
               return service->Handshake(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[1],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::Name, ::Info, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Name* req,
             ::Info* resp) {
               return service->Make(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[2],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::Empty, ::Transition, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Empty* req,
             ::Transition* resp) {
               return service->Reset(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[3],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::Action, ::Transition, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Action* req,
             ::Transition* resp) {
               return service->Step(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[4],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::RenderMode, ::RenderOut, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::RenderMode* req,
             ::RenderOut* resp) {
               return service->Render(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[5],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::EnvSeed, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::EnvSeed* req,
             ::Empty* resp) {
               return service->Seed(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[6],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::Empty, ::Action, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Empty* req,
             ::Action* resp) {
               return service->Sample(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      Env_method_names[7],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< Env::Service, ::Empty, ::Empty, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](Env::Service* service,
             ::grpc::ServerContext* ctx,
             const ::Empty* req,
             ::Empty* resp) {
               return service->Close(ctx, req, resp);
             }, this)));
}

Env::Service::~Service() {
}

::grpc::Status Env::Service::Handshake(::grpc::ServerContext* context, const ::Empty* request, ::MetaData* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Make(::grpc::ServerContext* context, const ::Name* request, ::Info* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Reset(::grpc::ServerContext* context, const ::Empty* request, ::Transition* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Step(::grpc::ServerContext* context, const ::Action* request, ::Transition* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Render(::grpc::ServerContext* context, const ::RenderMode* request, ::RenderOut* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Seed(::grpc::ServerContext* context, const ::EnvSeed* request, ::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Sample(::grpc::ServerContext* context, const ::Empty* request, ::Action* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Env::Service::Close(::grpc::ServerContext* context, const ::Empty* request, ::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


