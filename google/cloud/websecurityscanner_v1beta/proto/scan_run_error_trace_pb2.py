# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1beta/proto/scan_run_error_trace.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.websecurityscanner_v1beta.proto import (
    scan_config_error_pb2 as google_dot_cloud_dot_websecurityscanner__v1beta_dot_proto_dot_scan__config__error__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1beta/proto/scan_run_error_trace.proto",
    package="google.cloud.websecurityscanner.v1beta",
    syntax="proto3",
    serialized_options=b"\n*com.google.cloud.websecurityscanner.v1betaB\026ScanRunErrorTraceProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nGgoogle/cloud/websecurityscanner_v1beta/proto/scan_run_error_trace.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x44google/cloud/websecurityscanner_v1beta/proto/scan_config_error.proto"\x95\x03\n\x11ScanRunErrorTrace\x12L\n\x04\x63ode\x18\x01 \x01(\x0e\x32>.google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace.Code\x12R\n\x11scan_config_error\x18\x02 \x01(\x0b\x32\x37.google.cloud.websecurityscanner.v1beta.ScanConfigError\x12#\n\x1bmost_common_http_error_code\x18\x03 \x01(\x05"\xb8\x01\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x15\n\x11SCAN_CONFIG_ISSUE\x10\x02\x12\x1f\n\x1b\x41UTHENTICATION_CONFIG_ISSUE\x10\x03\x12\x1c\n\x18TIMED_OUT_WHILE_SCANNING\x10\x04\x12\x16\n\x12TOO_MANY_REDIRECTS\x10\x05\x12\x18\n\x14TOO_MANY_HTTP_ERRORS\x10\x06\x42\xc9\x01\n*com.google.cloud.websecurityscanner.v1betaB\x16ScanRunErrorTraceProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1betab\x06proto3',
    dependencies=[
        google_dot_cloud_dot_websecurityscanner__v1beta_dot_proto_dot_scan__config__error__pb2.DESCRIPTOR
    ],
)


_SCANRUNERRORTRACE_CODE = _descriptor.EnumDescriptor(
    name="Code",
    full_name="google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace.Code",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CODE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INTERNAL_ERROR",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SCAN_CONFIG_ISSUE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="AUTHENTICATION_CONFIG_ISSUE",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TIMED_OUT_WHILE_SCANNING",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TOO_MANY_REDIRECTS",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TOO_MANY_HTTP_ERRORS",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=407,
    serialized_end=591,
)
_sym_db.RegisterEnumDescriptor(_SCANRUNERRORTRACE_CODE)


_SCANRUNERRORTRACE = _descriptor.Descriptor(
    name="ScanRunErrorTrace",
    full_name="google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code",
            full_name="google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace.code",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="scan_config_error",
            full_name="google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace.scan_config_error",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="most_common_http_error_code",
            full_name="google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace.most_common_http_error_code",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SCANRUNERRORTRACE_CODE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=186,
    serialized_end=591,
)

_SCANRUNERRORTRACE.fields_by_name["code"].enum_type = _SCANRUNERRORTRACE_CODE
_SCANRUNERRORTRACE.fields_by_name[
    "scan_config_error"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1beta_dot_proto_dot_scan__config__error__pb2._SCANCONFIGERROR
)
_SCANRUNERRORTRACE_CODE.containing_type = _SCANRUNERRORTRACE
DESCRIPTOR.message_types_by_name["ScanRunErrorTrace"] = _SCANRUNERRORTRACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanRunErrorTrace = _reflection.GeneratedProtocolMessageType(
    "ScanRunErrorTrace",
    (_message.Message,),
    {
        "DESCRIPTOR": _SCANRUNERRORTRACE,
        "__module__": "google.cloud.websecurityscanner_v1beta.proto.scan_run_error_trace_pb2",
        "__doc__": """Output only. Defines an error trace message for a ScanRun.
  
  Attributes:
      code:
          Indicates the error reason code.
      scan_config_error:
          If the scan encounters SCAN_CONFIG_ISSUE error, this field has
          the error message encountered during scan configuration
          validation that is performed before each scan run.
      most_common_http_error_code:
          If the scan encounters TOO_MANY_HTTP_ERRORS, this field
          indicates the most common HTTP error code, if such is
          available. For example, if this code is 404, the scan has
          encountered too many NOT_FOUND responses.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace)
    },
)
_sym_db.RegisterMessage(ScanRunErrorTrace)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
