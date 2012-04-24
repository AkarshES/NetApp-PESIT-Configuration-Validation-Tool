import first
first.parse("block","""devices  {
                   device {
 
                                vendor "NETAPP"
  
                                product "LUN"
  
                                selector "round-robin 0"
 
                              getuid_callout "/sbin/scsi_id -g -u -s /block/%n"
  
                                prio_callout "/sbin/mpath_prio_alua /dev/%n"
  
                              features "1 queue_if_no_path"
  
                                hardware_handler "1 alua"
 
                              path_grouping_policy group_by_prio
  
                                failback immediate
  
                             path_checker directio
  
                                flush_on_last_del yes
  
                                max_fds 8192
  
                                rr_weight priorities
  
                               rr_min_io 10
                                                                                                                                                                                
                               no_path_retry fail
 
               }
}
""")
