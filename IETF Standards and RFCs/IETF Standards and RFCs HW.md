## IETF Standards and RFCs

#### The mission of the IETF is to make the Internet work better by producing high quality, relevant technical documents that influence the way people design, use, and manage the Internet.
#### This is important for providing a diversity Internet environment for all the human beings.

## Interesting Working Groups:

## 1. Codec Encoding for LossLess Archiving and Realtime transmission (cellar)
### Area:		
Applications and Real-Time Area (art)
### State： 
Active
### About:

The preservation of audiovisual materials faces challenges from technological obsolescence, analog media deterioration, and the use of proprietary formats that lack formal open standards. While obsolescence and material degradation are widely addressed, the standardization of open, transparent, self-descriptive, lossless formats remains an important mission to be undertaken by the open source community.

FFV1 is a lossless video codec and Matroska is an extensible media container based on EBML (Extensible Binary Meta Language), a binary XML format. There are open source implementations of both formats, and an increasing interest in and support for use of FFV1 and Matroska. However, there are concerns about the sustainability and credibility of existing specifications for the long-term use of these formats. These existing specifications require broader review and formalization in order to encourage widespread adoption.

There is also a need for a lossless audio format to complement the lossless video codec and container format. FLAC is a lossless audio codec that has seen widespread adoption in a number of different applications including archival applications. While there are open source implementations of the codec, no formal standards for either the codec itself or its use in container formats currently exist. Review and formalization of the FLAC codec standard and its use in Matroska container formats is needed for wider adoption.

## 2. Extensions for Scalable DNS Service Discovery (dnssd)
#### Area:
Internet Area (int)
#### State:
Active
#### About:

Zero configuration networking protocols are currently well suited to
discover services within the scope of a single link. In particular,
the DNS-SD [RFC 6763] and mDNS [RFC6762] protocol suite (sometimes
referred to using Apple Computer Inc.'s trademark, Bonjour) are
widely used for DNS-based service discovery and host name resolution
on a single link.

The DNS-SD/mDNS protocol suite is used in many scenarios including
home, campus, and enterprise networks. However, the zero configuration
mDNS protocol is constrained to link-local multicast scope by design,
and therefore cannot be used to discover services on remote links.

In a home network that consists of a single (possibly bridged) link,
users experience the expected discovery behavior; available services
appear because all devices share a common link. However, in multi-link
home networks (as envisaged by the homenet WG) or in routed campus or
enterprise networks, devices and users can only discover services on
the same link, which is a significant limitation. This has led to
calls, such as the Educause petition, to develop an appropriate service
discovery solution to span multiple links or to perform discovery across
a wide area, not necessarily on directly connected links.

In addition, the "Smart Energy Profile 2 Application Protocol Standard",
published by ZigBee Alliance and HomePlug Powerline Alliance specifies
the DNS-SD/mDNS protocol suite as the basis for its method of zero
configuration service discovery. However, its use of wireless mesh
multi-link subnets in conjunction with traditional routed networks will
require extensions to the DNS-SD/mDNS protocols to allow operation
across multiple links.

The scenarios in which multi-link service discovery is required may
be zero configuration environments, environments where administrative
configuration is supported, or a mixture of the two.

As demand for service discovery across wider area routed networks
grows, some vendors are beginning to ship proprietary solutions. It
is thus both timely and important that efforts to develop improved, 
scalable, autonomous service discovery solutions for routed networks 
are coordinated towards producing a single, standards-based solution.

## 3. Autonomic Networking Integrated Model and Approach (anima)
#### Area:
Operations and Management Area (ops)
#### State:
Active
#### About:

Autonomic networking refers to the self-managing characteristics
(configuration, protection, healing, and optimization) of distributed 
network elements, adapting to unpredictable changes while hiding 
intrinsic complexity from operators and users. Autonomic Networking, 
which often involves closed-loop control, is applicable to the complete 
network (functions) lifecycle (e.g. installation, commissioning, 
operating, etc). An autonomic function that works in a distributed way 
across various network elements is a candidate for protocol design. Such 
functions should allow central guidance and reporting, and co-existence 
with non-autonomic methods of management. The general objective of
this working group is to enable the progressive introduction of 
autonomic functions into operational networks, as well as reusable 
autonomic network infrastructure, in order to reduce the OpEx.

This work builds on definitions and design goals, as well as a simple
architecture model undertaken in the Network Management Research Group 
(NMRG) of the IRTF (See draft-irtf-nmrg-an-gap-analysis and its 
companion draft-irtf-nmrg-autonomic-network-definitions).

Elements of autonomic functions already exist today. However, all such 
functions today have their own discovery, node identification, 
negotiation, transport, messaging and security mechanisms as well as 
non-autonomic management interfaces. There is no common infrastructure 
for distributed functions. This leads to inefficiencies. Additionally, 
management and optimisation of operational device configurations is 
expensive, tedious, and prone to human error. A simple example is 
assigning address prefixes to network segments in a large and constantly 
changing network. Similarly, repair or bypassing of faults requires 
human intervention and causes significant down time.

This WG will develop a system of autonomic functions that carry out the
intentions of the network operator without the need for detailed low-
level management of individual devices. This will be done by providing a 
secure closed-loop interaction mechanism whereby network elements 
cooperate directly to satisfy management intent. The working group will 
develop a control paradigm where network processes coordinate their 
decisions and automatically translate them into local actions, based on 
various sources of information including operator-supplied configuration 
information or from the existing protocols, such as routing protocol, 
etc.

## 4. Network Virtualization Overlays (nvo3)
#### Area:
Routing Area (rtg)
#### State:
Active
#### About:

The purpose of the NVO3 WG is to develop a set of protocols and/or 
protocol extensions that enable network virtualization within a data 
center (DC) environment that assumes an IP-based underlay. An NVO3 
solution provides layer 2 and/or layer 3 services for virtual networks 
enabling multi-tenancy and workload mobility, addressing the issues 
described in the problem statement (including management and security), 
and consistent with the framework previously produced by the NVO3 WG.

The NVO3 WG will develop solutions for network virtualization based on 
the following architectural tenets:
- Support for an IP-based underlay data plane
- A logically centralized authority for network virtualization
Network virtualization approaches that do not adhere to these tenets are
explicitly outside of the scope of the NVO3 WG.

In pursuit of the solutions described above, the NVO3 WG will document 
an architecture for network virtualization within a data center 
environment.

The NVO3 WG may produce requirements for a network virtualization
control plane, and will select, extend, and/or develop one protocol
for each of the functional interfaces identified to support the
architecture. Such protocols are expected to fulfill the communication
requirements between an End Device and a Network Virtualization Edge
(NVE) in cases where the NVE is not co-resident with the End Device,
and between an NVE and the Network Virtualization Authority (NVA).
The internal mechanisms and protocols of a logically centralized NVA
are explicitly out of scope of the NVO3 WG. Architectural issues
raised by coexistence of multiple logically centralized control planes
in the same data center may be considered by the WG. Inter-DC
mechanisms are not in scope of the NVO3 WG at this time.

The NVO3 WG may produce requirements for network virtualization data 
planes based on encapsulation of virtual network traffic over an IP-
based underlay data plane. Such requirements should consider OAM and 
security. Based on these requirements the WG will select, extend, and/or 
develop one or more data plane encapsulation format(s).

Additionally, the WG may document common use-cases for NVO3 solutions.

The working group may choose to adopt a protocol or data encapsulation 
that was previously worked on outside the IETF as the basis for the WG's 
work. If the NVO3 WG anticipates the adoption of the technologies of 
another SDO as part of the selected protocols or data encapsulation, the 
NVO3 WG will first liaise with that SDO to ensure the compatibility of 
the approach.

The NVO3 WG will not consider solutions to network virtualization
within a data center environment based on extensions to BGP or LISP
protocols.
