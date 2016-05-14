# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: content_manifest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='content_manifest.proto',
  package='',
  serialized_pb='\n\x16\x63ontent_manifest.proto\"\xef\x02\n\x16\x43ontentManifestPayload\x12\x35\n\x08mappings\x18\x01 \x03(\x0b\x32#.ContentManifestPayload.FileMapping\x1a\x9d\x02\n\x0b\x46ileMapping\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x14\n\x0csha_filename\x18\x04 \x01(\x0c\x12\x13\n\x0bsha_content\x18\x05 \x01(\x0c\x12=\n\x06\x63hunks\x18\x06 \x03(\x0b\x32-.ContentManifestPayload.FileMapping.ChunkData\x12\x12\n\nlinktarget\x18\x07 \x01(\t\x1a\x61\n\tChunkData\x12\x0b\n\x03sha\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63rc\x18\x02 \x01(\x07\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x13\n\x0b\x63\x62_original\x18\x04 \x01(\r\x12\x15\n\rcb_compressed\x18\x05 \x01(\r\"\xec\x01\n\x17\x43ontentManifestMetadata\x12\x10\n\x08\x64\x65pot_id\x18\x01 \x01(\r\x12\x14\n\x0cgid_manifest\x18\x02 \x01(\x04\x12\x15\n\rcreation_time\x18\x03 \x01(\r\x12\x1b\n\x13\x66ilenames_encrypted\x18\x04 \x01(\x08\x12\x18\n\x10\x63\x62_disk_original\x18\x05 \x01(\x04\x12\x1a\n\x12\x63\x62_disk_compressed\x18\x06 \x01(\x04\x12\x15\n\runique_chunks\x18\x07 \x01(\r\x12\x15\n\rcrc_encrypted\x18\x08 \x01(\r\x12\x11\n\tcrc_clear\x18\t \x01(\r\"-\n\x18\x43ontentManifestSignature\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x42\x05H\x01\x90\x01\x00')




_CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA = _descriptor.Descriptor(
  name='ChunkData',
  full_name='ContentManifestPayload.FileMapping.ChunkData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha', full_name='ContentManifestPayload.FileMapping.ChunkData.sha', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc', full_name='ContentManifestPayload.FileMapping.ChunkData.crc', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='ContentManifestPayload.FileMapping.ChunkData.offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_original', full_name='ContentManifestPayload.FileMapping.ChunkData.cb_original', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_compressed', full_name='ContentManifestPayload.FileMapping.ChunkData.cb_compressed', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=297,
  serialized_end=394,
)

_CONTENTMANIFESTPAYLOAD_FILEMAPPING = _descriptor.Descriptor(
  name='FileMapping',
  full_name='ContentManifestPayload.FileMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='ContentManifestPayload.FileMapping.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='ContentManifestPayload.FileMapping.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='ContentManifestPayload.FileMapping.flags', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sha_filename', full_name='ContentManifestPayload.FileMapping.sha_filename', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sha_content', full_name='ContentManifestPayload.FileMapping.sha_content', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='ContentManifestPayload.FileMapping.chunks', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linktarget', full_name='ContentManifestPayload.FileMapping.linktarget', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=109,
  serialized_end=394,
)

_CONTENTMANIFESTPAYLOAD = _descriptor.Descriptor(
  name='ContentManifestPayload',
  full_name='ContentManifestPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mappings', full_name='ContentManifestPayload.mappings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTENTMANIFESTPAYLOAD_FILEMAPPING, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=394,
)


_CONTENTMANIFESTMETADATA = _descriptor.Descriptor(
  name='ContentManifestMetadata',
  full_name='ContentManifestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='depot_id', full_name='ContentManifestMetadata.depot_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid_manifest', full_name='ContentManifestMetadata.gid_manifest', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='ContentManifestMetadata.creation_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filenames_encrypted', full_name='ContentManifestMetadata.filenames_encrypted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_disk_original', full_name='ContentManifestMetadata.cb_disk_original', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cb_disk_compressed', full_name='ContentManifestMetadata.cb_disk_compressed', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_chunks', full_name='ContentManifestMetadata.unique_chunks', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc_encrypted', full_name='ContentManifestMetadata.crc_encrypted', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc_clear', full_name='ContentManifestMetadata.crc_clear', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=397,
  serialized_end=633,
)


_CONTENTMANIFESTSIGNATURE = _descriptor.Descriptor(
  name='ContentManifestSignature',
  full_name='ContentManifestSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='ContentManifestSignature.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=635,
  serialized_end=680,
)

_CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA.containing_type = _CONTENTMANIFESTPAYLOAD_FILEMAPPING;
_CONTENTMANIFESTPAYLOAD_FILEMAPPING.fields_by_name['chunks'].message_type = _CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA
_CONTENTMANIFESTPAYLOAD_FILEMAPPING.containing_type = _CONTENTMANIFESTPAYLOAD;
_CONTENTMANIFESTPAYLOAD.fields_by_name['mappings'].message_type = _CONTENTMANIFESTPAYLOAD_FILEMAPPING
DESCRIPTOR.message_types_by_name['ContentManifestPayload'] = _CONTENTMANIFESTPAYLOAD
DESCRIPTOR.message_types_by_name['ContentManifestMetadata'] = _CONTENTMANIFESTMETADATA
DESCRIPTOR.message_types_by_name['ContentManifestSignature'] = _CONTENTMANIFESTSIGNATURE

class ContentManifestPayload(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class FileMapping(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType

    class ChunkData(_message.Message):
      __metaclass__ = _reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _CONTENTMANIFESTPAYLOAD_FILEMAPPING_CHUNKDATA

      # @@protoc_insertion_point(class_scope:ContentManifestPayload.FileMapping.ChunkData)
    DESCRIPTOR = _CONTENTMANIFESTPAYLOAD_FILEMAPPING

    # @@protoc_insertion_point(class_scope:ContentManifestPayload.FileMapping)
  DESCRIPTOR = _CONTENTMANIFESTPAYLOAD

  # @@protoc_insertion_point(class_scope:ContentManifestPayload)

class ContentManifestMetadata(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTENTMANIFESTMETADATA

  # @@protoc_insertion_point(class_scope:ContentManifestMetadata)

class ContentManifestSignature(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTENTMANIFESTSIGNATURE

  # @@protoc_insertion_point(class_scope:ContentManifestSignature)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\001\220\001\000')
# @@protoc_insertion_point(module_scope)