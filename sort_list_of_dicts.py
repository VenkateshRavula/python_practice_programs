rack1 = {"name":"dcs-1", "rack_mounts":[{"location":"top-10", "mountUri":"/rest/mount", "topUSlot":42}]}
rack2 = {"name":"dcs-2", "rack_mounts":[{"location":"top-20", "mountUri":"/rest/mount", "topUSlot":30}]}

for i in rack1['rack_mounts']:
    for j in rack2['rack_mounts']:
	    if i['mountUri'] == j['mountUri'] or i['topUSlot'] == j['topUSlot']:
		    # updating the dictionaries
			i.update(j)
			break #no need to iterate remaining items in j since an item is already matched
		else:
		    # append this dict item into rack mount list
			self.current_resource.data['rack_mounts'].append(j)
