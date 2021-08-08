from pydantic import BaseModel
from datetime import datetime

from typing import Optional, Dict, Union, List


# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_service
class Tag(BaseModel):
    key: Optional[str]
    value: Optional[str]


class AwsvpcConfiguration(BaseModel):
    subnets: Optional[List[str]]
    securityGroups: Optional[List[str]]
    assignPublicIp: Optional[str]


class Secret(BaseModel):
    name: str
    valueFrom: str


class RepositoryCredentials(BaseModel):
    credentialsParameter: Optional[str]


class PortMapping(BaseModel):
    containerPort: Optional[int]
    hostPort: Optional[int]
    protocol: Optional[str]


class EnvironmentVariable(BaseModel):
    name: Optional[str]
    value: Optional[str]


class EnvironmentFile(BaseModel):
    name: Optional[str]
    type: Optional[str]


class MountPoint(BaseModel):
    sourceVolume: Optional[str]
    containerPath: Optional[str]
    readOnly: Optional[bool]


class MountedVolume(BaseModel):
    sourceContainer: Optional[str]
    readOnly: Optional[bool]


class Capabilities(BaseModel):
    add: Optional[List[str]]
    drop: Optional[List[str]]


class Device(BaseModel):
    hostPath: Optional[str]
    containerPath: Optional[str]
    permissions: Optional[List[str]]


class TemporaryFileSystem(BaseModel):
    containerPath: Optional[str]
    size: Optional[int]
    mountOptions: Optional[List[str]]


class LinuxParameters(BaseModel):
    capabilities: Optional[Capabilities]
    devices: Optional[List[Device]]
    initProcessEnabled: Optional[bool]
    sharedMemorySize: Optional[int]
    tmpfs: Optional[List[TemporaryFileSystem]]
    maxSwap: Optional[int]
    swappiness: Optional[int]


class Dependency(BaseModel):
    containerName: str
    condition: str


class Host(BaseModel):
    hostname: str
    ipAddress: str


class Ulimit(BaseModel):
    name: str
    softLimit: int
    hardLimit: int


class LogConfiguration(BaseModel):
    logDriver: str
    options: Optional[Dict[str, str]]
    secretOptions: Optional[List[Secret]]


class HealthCheck(BaseModel):
    command: List[str]

    interval: Optional[int]
    timeout: Optional[int]
    retries: Optional[int]
    startPeriod: Optional[int]


class SystemControl(BaseModel):
    namespace: Optional[str]
    value: Optional[str]


class ResourceRequirement(BaseModel):
    value: str
    type: str


class FirelensConfiguration(BaseModel):
    type: str
    options: Optional[Dict[str, str]]


class VolumeHost(BaseModel):
    sourcePath: Optional[str]


class DockerVolumeConfiguration(BaseModel):
    scope: Optional[str]
    autoprovision: Optional[bool]
    driver: Optional[str]
    driverOpts: Optional[Dict[str, str]]
    labels: Optional[Dict[str, str]]


class EfsAuthorizationConfig(BaseModel):
    accessPointId: Optional[str]
    iam: Optional[str]


class FsxWindowsFileServerVolumeConfigurationAuthorizationConfiguration(BaseModel):
    credentialsParameter: str
    domain: str


class FsxWindowsFileServerVolumeConfiguration(BaseModel):
    fileSystemId: str
    rootDirectory: str
    authorizationConfig: FsxWindowsFileServerVolumeConfigurationAuthorizationConfiguration


class EfsVolumeConfiguration(BaseModel):
    fileSystemId: str
    rootDirectory: Optional[str]
    transitEncryption: Optional[str]
    transitEncryptionPort: Optional[int]
    authorizationConfig: Optional[EfsAuthorizationConfig]


class Volume(BaseModel):
    name: Optional[str]
    host: Optional[VolumeHost]
    dockerVolumeConfiguration: Optional[DockerVolumeConfiguration]
    efsVolumeConfiguration: Optional[EfsVolumeConfiguration]
    fsxWindowsFileServerVolumeConfiguration: Optional[FsxWindowsFileServerVolumeConfiguration]


class ProxyConfiguration(BaseModel):
    type: Optional[str]
    containerName: str
    properties: Optional[List[Dict[str, Union[str, Dict[str, str]]]]]


class InterfaceAccelerator(BaseModel):
    deviceName: str
    deviceType: str


class EphemeralStorage(BaseModel):
    sizeInGiB: int


class LoadBalancer(BaseModel):
    targetGroupArn: Optional[str]
    loadBalancerName: Optional[str]
    containerName: Optional[str]
    containerPort: Optional[int]


class ServiceRegistry(BaseModel):
    registryArn: Optional[str]
    port: Optional[int]
    containerName: Optional[str]
    containerPort: Optional[int]


class CapacityProviderStrategy(BaseModel):
    capacityProvider: Optional[str]
    weight: Optional[int]
    base: Optional[int]


class DeploymentConfiguration(BaseModel):
    class DeploymentCiruitBreaker(BaseModel):
        enable: Optional[bool]
        rollback: Optional[bool]

    deploymentCircuitBreaker: Optional[DeploymentCiruitBreaker]
    maximumPercent: Optional[int]
    minimumhealthyPercent: Optional[int]


class NetworkConfiguration(BaseModel):
    class AwsvpcConfiguration(BaseModel):
        subnets: Optional[List[str]]
        securityGroups: Optional[List[str]]
        assignPublicIp: Optional[str]

    awsvpcConfiguration: Optional[AwsvpcConfiguration]


class Scale(BaseModel):
    value: Optional[float]
    unit: Optional[str]


class Event(BaseModel):
    id: Optional[str]
    createdAt: Optional[datetime]
    message: Optional[str]


class Deployment(BaseModel):
    id: Optional[str]
    status: Optional[str]
    taskDefinition: Optional[str]
    desiredCount: Optional[int]
    pendingCount: Optional[int]
    runningCount: Optional[int]
    failedTasks: Optional[int]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    capacityProviderStrategy: Optional[List[CapacityProviderStrategy]]
    launchType: Optional[str]
    platformVersion: Optional[str]
    networkConfiguration: Optional[NetworkConfiguration]
    rolloutState: Optional[str]
    rolloutStateReason: Optional[str]


class PlacementConstraint(BaseModel):
    type: Optional[str]
    expression: Optional[str]


class PlacementStrategies(BaseModel):
    type: Optional[str]
    field: Optional[str]


class TaskSet(BaseModel):
    id: Optional[str]
    taskSetArn: Optional[str]
    serviceArn: Optional[str]
    clusterArn: Optional[str]
    startedBy: Optional[str]
    externalId: Optional[str]
    status: Optional[str]
    taskDefinition: Optional[str]
    computedDesiredCount: Optional[int]
    pendingCount: Optional[int]
    runningCount: Optional[int]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    launchType: Optional[str]
    capacityProviderStrategy: Optional[CapacityProviderStrategy]
    platformVersion: Optional[str]
    networkConfiguration: Optional[NetworkConfiguration]
    loadBalancers: Optional[List[LoadBalancer]]
    serviceRegistries: Optional[List[ServiceRegistry]]
    scale: Optional[Scale]
    stabilityStatus: Optional[str]
    stabilityStatusAt: Optional[datetime]
    tags: Optional[List[Tag]]


class DeploymentController(BaseModel):
    type: Optional[str]


class Failure(BaseModel):
    arn: Optional[str]
    reason: Optional[str]
    detail: Optional[str]


class Attribute(BaseModel):
    name: Optional[str]
    value: Optional[str]
    targetType: Optional[str]
    targetId: Optional[str]


class ContainerDefinition(BaseModel):
    name: Optional[str]
    image: Optional[str]
    repositoryCredentials: Optional[RepositoryCredentials]
    cpu: Optional[Union[str, int]]
    memory: Optional[int]
    memoryReservation: Optional[int]
    links: Optional[List[str]]
    portMappints: Optional[List[PortMapping]]
    essential: Optional[bool]
    entrypoint: Optional[List[str]]
    command: Optional[List[str]]
    environment: Optional[List[EnvironmentVariable]]
    environmentFiles: Optional[List[EnvironmentFile]]
    mountPoints: Optional[List[MountPoint]]
    columesFrom: Optional[List[MountedVolume]]
    linuxParameters: Optional[LinuxParameters]
    secrets: Optional[List[str]]
    dependsOn: Optional[List[Dependency]]
    startTimeout: Optional[int]
    stopTimeout: Optional[int]
    hostname: Optional[str]
    user: Optional[str]
    workingDirectory: Optional[str]
    privileged: Optional[bool]
    readonlyRootFilesystem: Optional[bool]
    dnsServers: Optional[List[str]]
    dnsSearchDomains: Optional[List[str]]
    extraHosts: Optional[List[Host]]
    dockerSecurityOptions: Optional[List[str]]
    interactive: Optional[bool]
    pseudoTerminal: Optional[bool]
    dockerLabels: Optional[Dict[str, str]]
    ulimits: Optional[List[Ulimit]]
    logConfiguration: Optional[LogConfiguration]
    healthCheck: Optional[HealthCheck]
    systemControls: Optional[List[SystemControl]]
    resourceRequirements: Optional[List[ResourceRequirement]]
    firelensConfiguration: Optional[FirelensConfiguration]
    volumes: Optional[List[Volume]]
    placementConstraints: Optional[List[str]]
    requiresCompatibilities: Optional[List[str]]
    cpu: Optional[Union[str, int]]
    memory: Optional[str]
    tags: Optional[List[Tag]]
    pidMode: Optional[str]
    ipcMode: Optional[str]
    proxyConfiguration: Optional[ProxyConfiguration]
    interfaceAccelerators: Optional[List[InterfaceAccelerator]]
    ephemeralStorage: Optional[EphemeralStorage]


class Service(BaseModel):
    serviceArn: Optional[str]
    serviceName: Optional[str]
    clusterArn: Optional[str]
    loadBalancers: Optional[List[LoadBalancer]]
    serviceRegistries: Optional[List[ServiceRegistry]]
    status: Optional[str]
    desiredCount: Optional[int]
    runningCount: Optional[int]
    pendingCount: Optional[int]
    launchType: Optional[str]
    capacityProviderStrategy: Optional[CapacityProviderStrategy]
    platformVersion: Optional[str]
    taskDefinition: Optional[str]
    deploymentConfiguration: Optional[DeploymentConfiguration]
    taskSets: Optional[List[TaskSet]]
    deployments: Optional[List[Deployment]]
    roleArn: Optional[str]
    events: Optional[List[Event]]
    createdAt: Optional[datetime]
    placementConstraints: Optional[List[PlacementConstraint]]
    placementStrategy: Optional[List[PlacementStrategies]]
    networkConfiguration: Optional[NetworkConfiguration]
    healthCheckGracePeriodSeconds: Optional[int]
    schedulingStrategy: Optional[str]
    deploymentController: Optional[DeploymentController]
    tags: Optional[List[Tag]]
    createdBy: Optional[str]
    enableECSManagedTags: Optional[bool]
    propagateTags: Optional[str]
    enableExecuteCommand: Optional[bool]


class Cluster(BaseModel):
    clusterArns: Optional[List[str]]
    NextToken: Optional[str]


class TaskDefinition(BaseModel):
    taskDefinitionArn: Optional[str]
    containerDefinitions: List[ContainerDefinition]
    family: Optional[str]
    taskRoleArn: Optional[str]
    executionRoleArn: Optional[str]
    networkMode: Optional[str]
    revision: Optional[int]
    volumes: Optional[List[Optional[Volume]]]
    status: Optional[str]
    requiresAttributes: Optional[List[Attribute]]
    placementConstraints: Optional[List[PlacementConstraint]]
    compatibilities: Optional[List[str]]
    requiresCompatibilities: Optional[List[str]]
    cpu: Optional[Union[str, int]]
    memory: Optional[str]
    interfaceAccelerators: Optional[List[InterfaceAccelerator]]
    pidMode: Optional[str]
    ipcMode: Optional[str]
    proxyConfiguration: Optional[ProxyConfiguration]
    registeredAt: Optional[datetime]
    deregisteredAt: Optional[datetime]
    registeredBy: Optional[str]
    ephemeralStorage: Optional[EphemeralStorage]
