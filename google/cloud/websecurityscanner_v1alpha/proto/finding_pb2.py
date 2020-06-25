# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1alpha/proto/finding.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.websecurityscanner_v1alpha.proto import (
    finding_addon_pb2 as google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1alpha/proto/finding.proto",
    package="google.cloud.websecurityscanner.v1alpha",
    syntax="proto3",
    serialized_options=b"\n+com.google.cloud.websecurityscanner.v1alphaB\014FindingProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n;google/cloud/websecurityscanner_v1alpha/proto/finding.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x19google/api/resource.proto\x1a\x41google/cloud/websecurityscanner_v1alpha/proto/finding_addon.proto"\xe9\x08\n\x07\x46inding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x0c\x66inding_type\x18\x02 \x01(\x0e\x32<.google.cloud.websecurityscanner.v1alpha.Finding.FindingType\x12\x13\n\x0bhttp_method\x18\x03 \x01(\t\x12\x12\n\nfuzzed_url\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x18\n\x10reproduction_url\x18\x07 \x01(\t\x12\x11\n\tframe_url\x18\x08 \x01(\t\x12\x11\n\tfinal_url\x18\t \x01(\t\x12\x13\n\x0btracking_id\x18\n \x01(\t\x12R\n\x10outdated_library\x18\x0b \x01(\x0b\x32\x38.google.cloud.websecurityscanner.v1alpha.OutdatedLibrary\x12V\n\x12violating_resource\x18\x0c \x01(\x0b\x32:.google.cloud.websecurityscanner.v1alpha.ViolatingResource\x12V\n\x12vulnerable_headers\x18\x0f \x01(\x0b\x32:.google.cloud.websecurityscanner.v1alpha.VulnerableHeaders\x12\\\n\x15vulnerable_parameters\x18\r \x01(\x0b\x32=.google.cloud.websecurityscanner.v1alpha.VulnerableParameters\x12\x39\n\x03xss\x18\x0e \x01(\x0b\x32,.google.cloud.websecurityscanner.v1alpha.Xss"\xb6\x02\n\x0b\x46indingType\x12\x1c\n\x18\x46INDING_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rMIXED_CONTENT\x10\x01\x12\x14\n\x10OUTDATED_LIBRARY\x10\x02\x12\x11\n\rROSETTA_FLASH\x10\x05\x12\x10\n\x0cXSS_CALLBACK\x10\x03\x12\r\n\tXSS_ERROR\x10\x04\x12\x17\n\x13\x43LEAR_TEXT_PASSWORD\x10\x06\x12\x18\n\x14INVALID_CONTENT_TYPE\x10\x07\x12\x18\n\x14XSS_ANGULAR_CALLBACK\x10\x08\x12\x12\n\x0eINVALID_HEADER\x10\t\x12#\n\x1fMISSPELLED_SECURITY_HEADER_NAME\x10\n\x12&\n"MISMATCHING_SECURITY_HEADER_VALUES\x10\x0b:\x84\x01\xea\x41\x80\x01\n)websecurityscanner.googleapis.com/Finding\x12Sprojects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}B\x98\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0c\x46indingProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3',
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2.DESCRIPTOR,
    ],
)


_FINDING_FINDINGTYPE = _descriptor.EnumDescriptor(
    name="FindingType",
    full_name="google.cloud.websecurityscanner.v1alpha.Finding.FindingType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="FINDING_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MIXED_CONTENT",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OUTDATED_LIBRARY",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROSETTA_FLASH",
            index=3,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="XSS_CALLBACK",
            index=4,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="XSS_ERROR",
            index=5,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CLEAR_TEXT_PASSWORD",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_CONTENT_TYPE",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="XSS_ANGULAR_CALLBACK",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_HEADER",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MISSPELLED_SECURITY_HEADER_NAME",
            index=10,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MISMATCHING_SECURITY_HEADER_VALUES",
            index=11,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=883,
    serialized_end=1193,
)
_sym_db.RegisterEnumDescriptor(_FINDING_FINDINGTYPE)


_FINDING = _descriptor.Descriptor(
    name="Finding",
    full_name="google.cloud.websecurityscanner.v1alpha.Finding",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="finding_type",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.finding_type",
            index=1,
            number=2,
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
            name="http_method",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.http_method",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="fuzzed_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.fuzzed_url",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="body",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.body",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="description",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.description",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="reproduction_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.reproduction_url",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="frame_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.frame_url",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="final_url",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.final_url",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="tracking_id",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.tracking_id",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
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
            name="outdated_library",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.outdated_library",
            index=10,
            number=11,
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
            name="violating_resource",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.violating_resource",
            index=11,
            number=12,
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
            name="vulnerable_headers",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.vulnerable_headers",
            index=12,
            number=15,
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
            name="vulnerable_parameters",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.vulnerable_parameters",
            index=13,
            number=13,
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
            name="xss",
            full_name="google.cloud.websecurityscanner.v1alpha.Finding.xss",
            index=14,
            number=14,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_FINDING_FINDINGTYPE],
    serialized_options=b"\352A\200\001\n)websecurityscanner.googleapis.com/Finding\022Sprojects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}/findings/{finding}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=199,
    serialized_end=1328,
)

_FINDING.fields_by_name["finding_type"].enum_type = _FINDING_FINDINGTYPE
_FINDING.fields_by_name[
    "outdated_library"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._OUTDATEDLIBRARY
)
_FINDING.fields_by_name[
    "violating_resource"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._VIOLATINGRESOURCE
)
_FINDING.fields_by_name[
    "vulnerable_headers"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._VULNERABLEHEADERS
)
_FINDING.fields_by_name[
    "vulnerable_parameters"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._VULNERABLEPARAMETERS
)
_FINDING.fields_by_name[
    "xss"
].message_type = (
    google_dot_cloud_dot_websecurityscanner__v1alpha_dot_proto_dot_finding__addon__pb2._XSS
)
_FINDING_FINDINGTYPE.containing_type = _FINDING
DESCRIPTOR.message_types_by_name["Finding"] = _FINDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Finding = _reflection.GeneratedProtocolMessageType(
    "Finding",
    (_message.Message,),
    {
        "DESCRIPTOR": _FINDING,
        "__module__": "google.cloud.websecurityscanner_v1alpha.proto.finding_pb2",
        "__doc__": """A Finding resource represents a vulnerability instance identified
  during a ScanRun.
  
  Attributes:
      name:
          The resource name of the Finding. The name follows the format
          of ‘projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{
          scanRunId}/findings/{findingId}’. The finding IDs are
          generated by the system.
      finding_type:
          The type of the Finding.
      http_method:
          The http method of the request that triggered the
          vulnerability, in uppercase.
      fuzzed_url:
          The URL produced by the server-side fuzzer and used in the
          request that triggered the vulnerability.
      body:
          The body of the request that triggered the vulnerability.
      description:
          The description of the vulnerability.
      reproduction_url:
          The URL containing human-readable payload that user can
          leverage to reproduce the vulnerability.
      frame_url:
          If the vulnerability was originated from nested IFrame, the
          immediate parent IFrame is reported.
      final_url:
          The URL where the browser lands when the vulnerability is
          detected.
      tracking_id:
          The tracking ID uniquely identifies a vulnerability instance
          across multiple ScanRuns.
      outdated_library:
          An addon containing information about outdated libraries.
      violating_resource:
          An addon containing detailed information regarding any
          resource causing the vulnerability such as JavaScript sources,
          image, audio files, etc.
      vulnerable_headers:
          An addon containing information about vulnerable or missing
          HTTP headers.
      vulnerable_parameters:
          An addon containing information about request parameters which
          were found to be vulnerable.
      xss:
          An addon containing information reported for an XSS, if any.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.Finding)
    },
)
_sym_db.RegisterMessage(Finding)


DESCRIPTOR._options = None
_FINDING._options = None
# @@protoc_insertion_point(module_scope)
