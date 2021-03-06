def minimum_total_waiting_time(service_times):
    # Sort the service times in increasing order.
    service_times.sort()
    minimum_total_waiting_time = 0
    for i, service_time in enumerate(service_times):
        num_remaining_queries = len(service_times) - (i + 1)
        total_waiting_time += service_time * num_remaining_queries
    return minimum_total_waiting_time
