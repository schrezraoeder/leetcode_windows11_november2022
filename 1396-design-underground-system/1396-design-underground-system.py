# Note: watched https://www.youtube.com/watch?v=C-WgQDqOxHs yesterday 
class UndergroundSystem:

    def __init__(self):
        self.journeys = {} 
        self.average_time_map = {} # average_time_map[(stationA, stationB)] == (total_time_so_far_from_A_to_B, number_of_journeys_from_A_to_B)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        start_time = t 
        self.journeys[id] = (stationName, start_time) # {`<customer id>: (station, time_0)} 
        # whenever this customer `id` checks out at a station, we will remove them from the `journeys` map 
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        customer_check_in = self.journeys[id] # a tuple, (stationName, start_time)
        if (customer_check_in[0], stationName) in self.average_time_map: 
            previous_total_time_A_to_B, previous_number_journeys_A_to_B = self.average_time_map[(customer_check_in[0], stationName)] 
            new_journey_length = t - customer_check_in[1]
            self.average_time_map[(customer_check_in[0], stationName)] = ((previous_total_time_A_to_B + new_journey_length), (previous_number_journeys_A_to_B+1))
            del self.journeys[id] 
        else: 
            new_journey_length = t - self.journeys[id][1] 
            self.average_time_map[(customer_check_in[0], stationName)] = ((new_journey_length), 1) 
            del self.journeys[id]
            
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time_startStation_to_endStation, number_of_journeys_from_startStation_to_endStation = self.average_time_map[(startStation, endStation)]
        return total_time_startStation_to_endStation / number_of_journeys_from_startStation_to_endStation
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)