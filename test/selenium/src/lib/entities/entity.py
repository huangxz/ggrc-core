# Copyright (C) 2017 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
"""Create, description, representation and equal of entities."""
# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods


class Entity(object):
  """Class that represent model for base entity."""
  # pylint: disable=invalid-name
  # pylint: disable=redefined-builtin

  def __init__(self, title=None, id=None, href=None, url=None, type=None):
    self.title = title
    self.id = id
    self.href = href
    self.url = url
    self.type = type

  @staticmethod
  def attrs_names_all_entities():
    """Get list of all possible unique entities attributes' names."""
    all_entities_cls = [
        PersonEntity, CustomAttributeEntity, ProgramEntity,
        ControlEntity, AuditEntity, AssessmentEntity,
        AssessmentTemplateEntity, IssueEntity]
    all_entities_attrs_names = [
        entity_class().__dict__.keys() for
        entity_class in all_entities_cls]
    unique_entities_attrs_names = {
        val for sublist in all_entities_attrs_names for val in sublist}
    return unique_entities_attrs_names


class PersonEntity(Entity):
  """Class that represent model for Person."""
  __hash__ = None

  def __init__(self, email=None, authorizations=None):
    super(PersonEntity, self).__init__()
    self.email = email
    self.authorizations = authorizations

  def __repr__(self):
    return ("object_type: {type}, name: {name}, id: {id}, href: {href}, "
            "url: {url}, email: {email}, "
            "authorizations: {authorizations}").format(
        type=self.type, name=self.title, id=self.id, href=self.href,
        url=self.url, email=self.email, authorizations=self.authorizations)


class CustomAttributeEntity(object):
  """Class that represent model for Custom Attribute."""
  # pylint: disable=too-many-instance-attributes
  __hash__ = None

  def __init__(self, obj_id=None, title=None, ca_type=None,
               definition_type=None, helptext="", placeholder=None,
               multi_choice_options=None, is_mandatory=False, ca_global=True):
    super(CustomAttributeEntity, self).__init__()
    self.obj_id = obj_id
    self.title = title
    self.ca_type = ca_type
    self.definition_type = definition_type
    self.helptext = helptext
    self.placeholder = placeholder
    self.multi_choice_options = multi_choice_options
    self.is_mandatory = is_mandatory
    self.ca_global = ca_global

  def __repr__(self):
    return "{def_type}:{ca_type} {title};Mandatory:{mandatory}".format(
        ca_type=self.ca_type,
        title=self.title,
        mandatory=self.is_mandatory,
        def_type=self.definition_type)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and
            self.title == other.title and
            self.ca_type == other.ca_type and
            self.is_mandatory == other.is_mandatory and
            self.definition_type == other.definition_type)


class ProgramEntity(Entity):
  """Class that represent model for Program."""
  __hash__ = None

  def __init__(self, manager=None, primary_contact=None, code=None, state=None,
               last_update=None):
    super(ProgramEntity, self).__init__()
    self.manager = manager
    self.primary_contact = primary_contact
    self.code = code
    self.state = state
    self.last_update = last_update

  def __repr__(self):
    return ("object_type: {type}, title: {title}, id: {id}, href: {href}, "
            "url: {url}, manager: {manager}, "
            "primary contact: {primary_contact}, code: {code}, "
            "state: {state}, last update: {last_update}").format(
        type=self.type, title=self.title, id=self.id, href=self.href,
        url=self.url, manager=self.manager,
        primary_contact=self.primary_contact, code=self.code, state=self.state,
        last_update=self.last_update)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and self.type == other.type and
            self.title == other.title and self.code == other.code and
            self.manager == other.manager and self.state == other.state and
            self.primary_contact == other.primary_contact)


class ControlEntity(Entity):
  """Class that represent model for Control."""
  __hash__ = None

  def __init__(self, owner=None, primary_contact=None, code=None, state=None,
               last_update=None):
    super(ControlEntity, self).__init__()
    self.owner = owner
    self.primary_contact = primary_contact
    self.code = code
    self.state = state
    self.last_update = last_update

  def __repr__(self):
    return ("object_type: {type}, title: {title}, id: {id}, href: {href}, "
            "url: {url}, owner: {owner}, primary contact: {primary_contact}, "
            "code: {code}, state: {state}, last update: {last_update}").format(
        type=self.type, title=self.title, id=self.id, href=self.href,
        url=self.url, owner=self.owner, primary_contact=self.primary_contact,
        code=self.code, state=self.state, last_update=self.last_update)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and self.type == other.type and
            self.title == other.title and self.code == other.code and
            self.state == other.state and self.owner == other.owner and
            self.primary_contact == other.primary_contact)

  def __lt__(self, other):
    return self.code < other.code


class AuditEntity(Entity):
  """Class that represent model for Audit."""
  __hash__ = None

  def __init__(self, program=None, audit_lead=None, code=None,
               status=None, last_update=None):
    super(AuditEntity, self).__init__()
    self.program = program
    self.audit_lead = audit_lead
    self.code = code
    self.status = status
    self.last_update = last_update

  def __repr__(self):
    return (
        "object_type: {type}, title: {title}, id: {id}, href: {href}, "
        "url: {url}, program: {program}, audit lead: {audit_lead}, "
        "code: {code}, status: {status}, last update: {last_update}").format(
            type=self.type, title=self.title, id=self.id, href=self.href,
            url=self.url, program=self.program, audit_lead=self.audit_lead,
            code=self.code, status=self.status, last_update=self.last_update)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and self.type == other.type and
            self.title == other.title and self.code == other.code and
            self.audit_lead == other.audit_lead and
            self.status == other.status)


class AssessmentTemplateEntity(Entity):
  """Class that represent model for Assessment Template."""
  # pylint: disable=superfluous-parens

  __hash__ = None

  def __init__(self, audit=None, asmt_objects=None, def_assessors=None,
               def_verifiers=None, code=None, last_update=None):
    super(AssessmentTemplateEntity, self).__init__()
    self.audit = audit
    self.asmt_objects = asmt_objects
    self.def_assessors = def_assessors
    self.def_verifiers = def_verifiers
    self.code = code
    self.last_update = last_update

  def __repr__(self):
    return ("object_type: {type}, title: {title}, id: {id}, href: {href}, "
            "url: {url}, audit: {audit}, assessment objects: {asmt_objects}, "
            "default assessors: {def_assessors}, "
            "default verifiers: {def_verifiers}, code: {code}, "
            "last update: {last_update}").format(
        type=self.type, title=self.title, id=self.id, href=self.href,
        url=self.url, audit=self.audit, asmt_objects=self.asmt_objects,
        def_assessors=self.def_assessors, def_verifiers=self.def_verifiers,
        code=self.code, last_update=self.last_update)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and self.type == other.type and
            self.title == other.title and self.code == other.code)


class AssessmentEntity(Entity):
  """Class that represent model for Assessment."""
  # pylint: disable=too-many-instance-attributes
  # pylint: disable=redefined-builtin
  __hash__ = None

  def __init__(self, object=None, audit=None, creators=None, assignees=None,
               primary_contact=None, is_verified=None, code=None, state=None,
               last_update=None):
    super(AssessmentEntity, self).__init__()
    self.object = object
    self.audit = audit
    self.creators = creators
    self.assignees = assignees
    self.primary_contact = primary_contact
    self.is_verified = is_verified
    self.code = code
    self.state = state
    self.last_update = last_update

  def __repr__(self):
    return ("object_type: {type}, title: {title}, id: {id}, href: {href}, "
            "url: {url}, object: {object}, audit: {audit}, "
            "creators: {creators}, assignees: {assignees}, "
            "primary_contact: {primary_contact}, is_verified: {is_verified}, "
            "code: {code}, state: {state}, last update: {last_update}").format(
        type=self.type, title=self.title, id=self.id, href=self.href,
        url=self.url, object=self.object, audit=self.audit,
        creators=self.creators, assignees=self.assignees,
        primary_contact=self.primary_contact, is_verified=self.is_verified,
        code=self.code, state=self.state, last_update=self.last_update)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and self.type == other.type and
            self.title == other.title and self.code == other.code and
            self.state == other.state and
            self.is_verified == other.is_verified)


class IssueEntity(Entity):
  """Class that represent model for Issue."""
  # pylint: disable=too-many-instance-attributes
  __hash__ = None

  def __init__(self, audit=None, owner=None, primary_contact=None, code=None,
               state=None, last_update=None):
    super(IssueEntity, self).__init__()
    self.audit = audit
    self.owner = owner
    self.primary_contact = primary_contact
    self.code = code
    self.state = state
    self.last_update = last_update

  def __repr__(self):
    return ("object_type: {type}, title: {title}, id: {id}, href: {href}, "
            "url: {url}, audit: {audit}, owner: {owner}, "
            "primary_contact: {primary_contact}, code: {code}, "
            "state: {state}, last update: {last_update}").format(
        type=self.type, title=self.title, id=self.id, href=self.href,
        url=self.url, audit=self.audit, owner=self.owner,
        primary_contact=self.primary_contact, code=self.code, state=self.state,
        last_update=self.last_update)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and self.type == other.type and
            self.title == other.title and self.owner == other.owner,
            self.code == other.code and self.state == other.state)
