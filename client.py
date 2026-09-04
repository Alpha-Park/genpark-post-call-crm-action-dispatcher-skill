class PostCallCrmActionDispatcherClient:
    def dispatch_call_summary(self, call_id='call_7721', transcript='Customer inquired about solar installation...', call_duration_seconds=184):
        return {
            'dispatch_id': 'crm_dsp_7721',
            'call_id': call_id,
            'call_sentiment': 'HIGHLY_INTERESTED_PROSPECT',
            'lead_score': 92,
            'crm_record_created': True,
            'hubspot_deal_id': 'deal_solar_9918',
            'calendar_invite_sent': True,
            'crm_webhook_audit_url': 'https://synthflow.crm.genpark.ai/dispatches/7721.json'
        }
