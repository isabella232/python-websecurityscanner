# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1beta/proto/crawled_url.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1beta/proto/crawled_url.proto",
    package="google.cloud.websecurityscanner.v1beta",
    syntax="proto3",
    serialized_options=b"\n*com.google.cloud.websecurityscanner.v1betaB\017CrawledUrlProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n>google/cloud/websecurityscanner_v1beta/proto/crawled_url.proto\x12&google.cloud.websecurityscanner.v1beta"<\n\nCrawledUrl\x12\x13\n\x0bhttp_method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\tB\xc2\x01\n*com.google.cloud.websecurityscanner.v1betaB\x0f\x43rawledUrlProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1betab\x06proto3',
)


_CRAWLEDURL = _descriptor.Descriptor(
    name="CrawledUrl",
    full_name="google.cloud.websecurityscanner.v1beta.CrawledUrl",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="http_method",
            full_name="google.cloud.websecurityscanner.v1beta.CrawledUrl.http_method",
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
            name="url",
            full_name="google.cloud.websecurityscanner.v1beta.CrawledUrl.url",
            index=1,
            number=2,
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
            full_name="google.cloud.websecurityscanner.v1beta.CrawledUrl.body",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=106,
    serialized_end=166,
)

DESCRIPTOR.message_types_by_name["CrawledUrl"] = _CRAWLEDURL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CrawledUrl = _reflection.GeneratedProtocolMessageType(
    "CrawledUrl",
    (_message.Message,),
    {
        "DESCRIPTOR": _CRAWLEDURL,
        "__module__": "google.cloud.websecurityscanner_v1beta.proto.crawled_url_pb2",
        "__doc__": """A CrawledUrl resource represents a URL that was crawled during a
  ScanRun. Web Security Scanner Service crawls the web applications,
  following all links within the scope of sites, to find the URLs to
  test against.
  
  Attributes:
      http_method:
          The http method of the request that was used to visit the URL,
          in uppercase.
      url:
          The URL that was crawled.
      body:
          The body of the request that was used to visit the URL.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.CrawledUrl)
    },
)
_sym_db.RegisterMessage(CrawledUrl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
