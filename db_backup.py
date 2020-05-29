# from subprocess import PIPE,Popen
# import shlex

# def dump_table(host_name,database_name,user_name,database_password,table_name):

#     # command = 'pg_dump -h {0} -d {1} -U {2} -p 5432 -t public.{3} -Fc -f /tmp/table.dmp'\
#     # .format(host_name,database_name,user_name,table_name)

#     command = 'sudo pg_dump  -d aiops -U postgres -t public.configuration_tbl'

#     p = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)

#     p.communicate('{}\n'.format('postgres'))

#     return "Success"

# def restore_table(host_name,database_name,user_name,database_password):

#     #Remove the '<' from the pg_restore command.
#     command = 'pg_restore -h {0} -d {1} -U {2} /tmp/table.dmp'\
#               .format(host_name,database_name,user_name)

#     #Use shlex to use a list of parameters in Popen instead of using the
#     #command as is.
#     command = shlex.split(command)

#     #Let the shell out of this (i.e. shell=False)
#     p = Popen(command,shell=False,stdin=PIPE,stdout=PIPE,stderr=PIPE)

#     return p.communicate('{}\n'.format(database_password))

# def main():
#     dump_table('localhost','sprint30','postgres','postgres','configuration_tbl')
#     # restore_table('localhost','testdb','user_name','passwd')

# if __name__ == "__main__":
#     main()
# tables=['public.priority_change','public.alerts_jenkins2','public.bk_inc_std','public.action_mapping_tbl','public.category_master_tbl','public.template_tbl','public.config_tbl','public.incident_std_tbl','public.tickets_jenkins1','public.alerts_jenkins1','public.munira','public.sop_tbl','public.alerts_tbl','public.tickets_jenkins2','public.association_rules','public.assigned_to_change','public.alerts_rejected','public.api_meta','public.api_meta_2','public.assignment_group_change','public.broker_meta','public.business_audit_daily','public.category','public.category_counts','public.category_sop_mapping','public.cmdb_master_health','public.configuration_tbl','public.db_config_tbl','public.cmdb_master_with_health_view','public.correlation_tbl','public.df_incident','public.email_tbl','public.es_email_config_tbl','public.es_email_tbl','public.es_kafka_config_tbl','public.event_cor','public.incident_config_tbl','public.event_correlation_data','public.final_event_corr','public.network_graph_corr_app_x_y_new','public.hierarchy_view','public.incident_resolution_mapping','public.incident_stage_snow','public.incident_state_change','public.kpi_formulaes','public.lookup_data_new','public.lookup_data','public.mapping_sop_resolution','public.incident_category_mapping','public.nagios_stage_tbl','public.ps_column_mapper_tbl','public.new_association_rules','public.newrelic_stage_tbl','public.notification_reports_config','public.parent_child_mapping','public.resolution_tbl','public.saved_alerts_temp','public.solarwinds_stage_tbl','public.mustafa','public.incident_resolution_mapping','public.incident_stage_snow','public.incident_category_mapping','public.incident_config_tbl','public.event_correlation_data','public.event_cor','public.df_incident','public.db_config_tbl','public.correlation_tbl','public.configuration_tbl','public.api_meta','public.incident_std_tbl','public.business_audit_daily','public.cmdb_master_health','public.category_sop_mapping','public.category','public.category_counts','public.broker_meta','public.association_rules','public.assignment_group_change','public.assigned_to_change','public.final_event_corr','public.alerts_rejected','rule_engine.re_source_config_tbl','rule_engine.health_colour_matrix','rule_engine.ci_health_catalog_tbl','rule_engine.ci_health_severity_config','scheduler.trusted_sites','scheduler.scheduler_staging_tbl','scheduler.audit_logs','scheduler.scheduler_master_tbl','action_manager.automation_values_mapper','aiops_automation.automation_activity_logs','aiops_automation.automation_ayehu','aiops_automation.automation_braio','aiops_automation.interface_fields_mapper','aiops_automation.automation_input_details','aiops_automation.automation_execution_audit','aiops_automation.automation_master','aiops_automation.incident_sop_automation','aiops_automation.sop_automation_mapping','aiops_automation.automation_snow','cmdb.hardware','cmdb.bus_app_bkup','cmdb.application','cmdb.relationship_type','cmdb.api_meta','cmdb.asset_type','cmdb.asset_status','cmdb.ci_list','cmdb.business_application_details','cmdb.cmdb_master','cmdb.assets','cmdb.cmdb_relationship','cmdb.continent_details','cmdb.health_colour_matrix','cmdb.location','cmdb.related_assets','cognitive.source_config_tbl','cognitive.kafka_config_tbl','dam.metric_catalog','dam.metric_definition','dam.ticket_kpi','dam.ticket_sla_meta','email_parser.kafka_config_tbl','email_parser.email_stg_tbl','email_parser.email_config_tbl','mosaic_connector.connector_config_tbl','mosaic_parser.ps_source_config_tbl','mosaic_parser.ps_column_mapper_tbl','mosaic_parser.ps_kafka_config_tbl','notification.config_tbl','notification.template_tbl']

table_dict={'public.priority_change':'Operational','public.action_mapping_tbl':'Configuration','public.category_master_tbl':'Seed','public.template_tbl':'Configuration','public.config_tbl':'Configuration','public.incident_std_tbl':'Operational','public.sop_tbl':'Seed','public.alerts_tbl':'Operational','public.association_rules':'Configuration','public.assigned_to_change':'Operational','public.alerts_rejected':'Operational','public.api_meta':'Configuration','public.assignment_group_change':'Operational','public.broker_meta':'Configuration','public.business_audit_daily':'Operational','public.category':'Operational','public.category_counts':'Operational','public.category_sop_mapping':'Operational','public.cmdb_master_health':'Operational','public.configuration_tbl':'Configuration','public.db_config_tbl':'Configuration','public.cmdb_master_with_health_view':'Operational','public.correlation_tbl':'Operational','public.df_incident':'Operational','public.email_tbl':'Configuration','public.es_email_config_tbl':'Configuration','public.es_email_tbl':'Configuration','public.es_kafka_config_tbl':'Configuration','public.event_cor':'Operational','public.incident_config_tbl':'Configuration','public.event_correlation_data':'Operational','public.final_event_corr':'Operational','public.network_graph_corr_app_x_y_new':'Operational','public.hierarchy_view':'Operational','public.incident_stage_snow':'Operational','public.incident_state_change':'Operational','public.kpi_formulaes':'Configuration','public.lookup_data_new':'Operational','public.lookup_data':'Operational','public.incident_category_mapping':'Operational','public.nagios_stage_tbl':'Operational','public.ps_column_mapper_tbl':'Configuration','public.new_association_rules':'Seed','public.newrelic_stage_tbl':'Operational','public.notification_reports_config':'Configuration','public.parent_child_mapping':'Operational','public.saved_alerts_temp':'Operational','public.solarwinds_stage_tbl':'Operational','rule_engine.re_source_config_tbl':'Configuration','rule_engine.health_colour_matrix':'Configuration','rule_engine.ci_health_catalog_tbl':'Configuration','rule_engine.ci_health_severity_config':'Configuration','scheduler.trusted_sites':'Operational','scheduler.scheduler_staging_tbl':'Operational','scheduler.audit_logs':'Operational','scheduler.scheduler_master_tbl':'Operational','action_manager.automation_values_mapper':'Configuration','aiops_automation.automation_activity_logs':'Operational','aiops_automation.automation_ayehu':'Operational','aiops_automation.automation_braio':'Operational','aiops_automation.interface_fields_mapper':'Configuration','aiops_automation.automation_input_details':'Configuration','aiops_automation.automation_execution_audit':'Operational','aiops_automation.automation_master':'Operational','aiops_automation.incident_sop_automation':'Operational','aiops_automation.sop_automation_mapping':'Operational','aiops_automation.automation_snow':'Operational','cmdb.hardware':'Operational','cmdb.application':'Operational','cmdb.relationship_type':'Operational','cmdb.api_meta':'Operational','cmdb.asset_type':'Operational','cmdb.asset_status':'Operational','cmdb.ci_list':'Operational','cmdb.business_application_details':'Operational','cmdb.cmdb_master':'Operational','cmdb.assets':'Operational','cmdb.cmdb_relationship':'Operational','cmdb.continent_details':'Operational','cmdb.health_colour_matrix':'Operational','cmdb.location':'Operational','cmdb.related_assets':'Operational','cognitive.source_config_tbl':'Configuration','cognitive.kafka_config_tbl':'Configuration','dam.metric_catalog':'Configuration','dam.metric_definition':'Configuration','dam.ticket_kpi':'Operational','dam.ticket_sla_meta':'Configuration','email_parser.kafka_config_tbl':'Configuration','email_parser.email_stg_tbl':'Operational','email_parser.email_config_tbl':'Configuration','mosaic_connector.connector_config_tbl':'Configuration','mosaic_parser.ps_source_config_tbl':'Configuration','mosaic_parser.ps_column_mapper_tbl':'Configuration','mosaic_parser.ps_kafka_config_tbl':'Configuration','notification.config_tbl':'Configuration','notification.template_tbl':'Configuration'}
from sh import pg_dump
count=0
with open('temp_all.sql', 'w') as f:
	# for table in tables:
	# 	pg_dump('-h', 'localhost', '-U', 'postgres', '-t',table, '--column-inserts', 'sprint30', _out=f)
	# 	print(count)
	# 	count=count+1
	pg_dump('-h', 'localhost', '-U', 'postgres', '--schema-only', 'sprint30', _out=f)
	for key, value in table_dict.items():
		if value=='Operational':
			# pg_dump('-h', 'localhost', '-U', 'postgres', '-t',key, '--schema-only', 'sprint30', _out=f)
			pass
		else:
			pg_dump('-h', 'localhost', '-U', 'postgres', '-t',key, '--column-inserts', '--data-only', 'sprint30', _out=f)
		print(count)
		count=count+1