# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jaccount.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='jaccount.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0ejaccount.proto\"\x1d\n\x0c\x43\x61ptchaNonce\x12\r\n\x05nonce\x18\x01 \x01(\t\"6\n\x0c\x43\x61ptchaImage\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x10\n\x08img_blob\x18\x02 \x01(\x0c\":\n\tLoginForm\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06passwd\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61ptcha\x18\x03 \x01(\t\"3\n\x0fGeneralResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2p\n\x0fJaccountService\x12*\n\nGetCaptcha\x12\r.CaptchaNonce\x1a\r.CaptchaImage\x12\x31\n\x11SubmitCredentials\x12\n.LoginForm\x1a\x10.GeneralResponseb\x06proto3')
)

_CAPTCHANONCE = _descriptor.Descriptor(
    name='CaptchaNonce',
    full_name='CaptchaNonce',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='nonce', full_name='CaptchaNonce.nonce', index=0,
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
    serialized_start=18,
    serialized_end=47,
)

_CAPTCHAIMAGE = _descriptor.Descriptor(
    name='CaptchaImage',
    full_name='CaptchaImage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='content_type', full_name='CaptchaImage.content_type', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='img_blob', full_name='CaptchaImage.img_blob', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
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
    serialized_start=49,
    serialized_end=103,
)

_LOGINFORM = _descriptor.Descriptor(
    name='LoginForm',
    full_name='LoginForm',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='user', full_name='LoginForm.user', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='passwd', full_name='LoginForm.passwd', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='captcha', full_name='LoginForm.captcha', index=2,
            number=3, type=9, cpp_type=9, label=1,
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
    serialized_start=105,
    serialized_end=163,
)

_GENERALRESPONSE = _descriptor.Descriptor(
    name='GeneralResponse',
    full_name='GeneralResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='success', full_name='GeneralResponse.success', index=0,
            number=1, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='message', full_name='GeneralResponse.message', index=1,
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
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=165,
    serialized_end=216,
)

DESCRIPTOR.message_types_by_name['CaptchaNonce'] = _CAPTCHANONCE
DESCRIPTOR.message_types_by_name['CaptchaImage'] = _CAPTCHAIMAGE
DESCRIPTOR.message_types_by_name['LoginForm'] = _LOGINFORM
DESCRIPTOR.message_types_by_name['GeneralResponse'] = _GENERALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CaptchaNonce = _reflection.GeneratedProtocolMessageType('CaptchaNonce', (_message.Message,), dict(
    DESCRIPTOR=_CAPTCHANONCE,
    __module__='jaccount_pb2'
    # @@protoc_insertion_point(class_scope:CaptchaNonce)
))
_sym_db.RegisterMessage(CaptchaNonce)

CaptchaImage = _reflection.GeneratedProtocolMessageType('CaptchaImage', (_message.Message,), dict(
    DESCRIPTOR=_CAPTCHAIMAGE,
    __module__='jaccount_pb2'
    # @@protoc_insertion_point(class_scope:CaptchaImage)
))
_sym_db.RegisterMessage(CaptchaImage)

LoginForm = _reflection.GeneratedProtocolMessageType('LoginForm', (_message.Message,), dict(
    DESCRIPTOR=_LOGINFORM,
    __module__='jaccount_pb2'
    # @@protoc_insertion_point(class_scope:LoginForm)
))
_sym_db.RegisterMessage(LoginForm)

GeneralResponse = _reflection.GeneratedProtocolMessageType('GeneralResponse', (_message.Message,), dict(
    DESCRIPTOR=_GENERALRESPONSE,
    __module__='jaccount_pb2'
    # @@protoc_insertion_point(class_scope:GeneralResponse)
))
_sym_db.RegisterMessage(GeneralResponse)

_JACCOUNTSERVICE = _descriptor.ServiceDescriptor(
    name='JaccountService',
    full_name='JaccountService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=218,
    serialized_end=330,
    methods=[
        _descriptor.MethodDescriptor(
            name='GetCaptcha',
            full_name='JaccountService.GetCaptcha',
            index=0,
            containing_service=None,
            input_type=_CAPTCHANONCE,
            output_type=_CAPTCHAIMAGE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='SubmitCredentials',
            full_name='JaccountService.SubmitCredentials',
            index=1,
            containing_service=None,
            input_type=_LOGINFORM,
            output_type=_GENERALRESPONSE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_JACCOUNTSERVICE)

DESCRIPTOR.services_by_name['JaccountService'] = _JACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
