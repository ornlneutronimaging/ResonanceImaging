def calculate_average_ob_data(ob_data):
    '''
    Calculate the average OB
    '''
    sum_ob_data = ob_data[0]
    if len(ob_data) == 1:
        return sum_ob_data
    else:
        for _index in range(1, len(ob_data)):
            _ob = ob_data[_index]
            sum_ob_data += _ob
        
    mean_ob_data = sum_ob_data / len(ob_data)
    return mean_ob_data


def normalized_data_by_ob_file(data, mean_ob_data):
    '''
    return normalized data using (I-I0)/I0 where
    I is the pixel value of the data
    I0 is the pixel value of the open beam
    '''
    
    normalized_data = []
    for _index, _data in enumerate(data):
        _normalized_data = (_data - mean_ob_data) / (mean_ob_data)
        normalized_data.append(_normalized_data)
        
    return normalized_data
