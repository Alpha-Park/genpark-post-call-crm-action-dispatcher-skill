from client import PostCallCrmActionDispatcherClient

def main():
    client = PostCallCrmActionDispatcherClient()
    res = client.dispatch_call_summary('call_test_01', 'Lead agreed to quote demo', 120)
    print('CRM Action Dispatcher: ' + res['dispatch_id'] + ' (' + res['call_sentiment'] + ')')
    print('Lead Score: ' + str(res['lead_score']) + ' | Deal ID: ' + res['hubspot_deal_id'])
    print('Audit URL: ' + res['crm_webhook_audit_url'])

if __name__ == '__main__':
    main()
