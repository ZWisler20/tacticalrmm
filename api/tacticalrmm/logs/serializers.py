from clients.serializers import SiteMinimumSerializer
from rest_framework import serializers

from .models import AuditLog, DebugLog, PendingAction


class AuditLogSerializer(serializers.ModelSerializer):
    entry_time = serializers.SerializerMethodField()
    ip_address = serializers.ReadOnlyField(source="debug_info.ip")
    site = serializers.SerializerMethodField()

    def get_site(self, obj):
        from agents.models import Agent
        from clients.serializers import SiteMinimumSerializer

        if obj.agent_id and Agent.objects.filter(agent_id=obj.agent_id).exists():
            return SiteMinimumSerializer(
                Agent.objects.get(agent_id=obj.agent_id).site
            ).data
        else:
            return None

    class Meta:
        model = AuditLog
        fields = "__all__"

    def get_entry_time(self, log):
        tz = self.context["default_tz"]
        return log.entry_time.astimezone(tz).strftime("%m %d %Y %H:%M:%S")


class PendingActionSerializer(serializers.ModelSerializer):
    hostname = serializers.ReadOnlyField(source="agent.hostname")
    client = serializers.ReadOnlyField(source="agent.client.name")
    site = serializers.ReadOnlyField(source="agent.site.name")
    due = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()

    class Meta:
        model = PendingAction
        fields = "__all__"


class DebugLogSerializer(serializers.ModelSerializer):
    agent = serializers.ReadOnlyField(source="agent.hostname")
    entry_time = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DebugLog
        fields = "__all__"

    def get_entry_time(self, log):
        tz = self.context["default_tz"]
        return log.entry_time.astimezone(tz).strftime("%m %d %Y %H:%M:%S")
