# All decimal 3 places
import math
# Function to compute mean
def mean(first_list):
    # mean Logic 
    if(len(first_list)==0):
        return 0
    summation_value = summation(first_list)
    mean_value = summation_value/len(first_list)
    mean_value = round(mean_value,6)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    if (len(first_list)==0):
        return 0
    variance_value = variance(first_list)
    standard_deviation_value = math.sqrt(variance_value)
    standard_deviation_value = round(standard_deviation_value,6)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    if (len(first_list)==0):
        return 0
    for i in first_list:
        if (isinstance(i,(int,float))==False):
            return 0
    mean_value  = mean(first_list)
    sum_value = 0
    for i in first_list:
        sum_value += ((i-mean_value)*(i-mean_value))
    variance_value = sum_value/len(first_list)
    variance_value = round(variance_value,6)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if (len(first_list) != len(second_list)):
        return 0
    # If the length of the list is zero then return 0
    if (len(first_list)==0):
        return 0
    mean_square_error_value = mse(first_list, second_list)
    rmse_value = math.sqrt(mean_square_error_value)
    rmse_value = round(rmse_value,6)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if (len(first_list) != len(second_list)):
        return 0
    # If the length of the list is zero then return 0
    if (len(first_list)==0):
        return 0
    for (i,j) in zip(first_list,second_list):
        if ((isinstance(i,(int,float))==False) or (isinstance(j,(int,float))==False)):
            return 0
    mean_square_value = 0
    for (i,j) in zip(first_list, second_list):
        mean_square_value += ((i-j)*(i-j))
    mse_value = mean_square_value/len(first_list)
    mse_value = round(mse_value,6)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if (len(first_list) != len(second_list)):
        return 0
    # If the length of the list is zero then return 0
    if (len(first_list)==0):
        return 0
    for (i,j) in zip(first_list,second_list):
        if ((isinstance(i,(int,float))==False) or (isinstance(j,(int,float))==False)):
            return 0
    mae_value =0
    for (i,j) in zip(first_list, second_list):
        mae_value += abs(i-j)
    mae_value /= len(first_list)
    mae_value = round(mae_value,6)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    # If the length of first list is different from second list then returning zero
    if (len(first_list) != len(second_list)):
        return 0
    # If the length of the list is zero then return 0
    if (len(first_list)==0):
        return 0
    for (i,j) in zip(first_list,second_list):
        if ((isinstance(i,(int,float))==False) or (isinstance(j,(int,float))==False)):
            return 0
    numerator_value = 0
    denominator_value = 0
    list1_mean_value = mean(first_list)
    for (i,j) in zip(first_list,second_list):
        numerator_value += ((i-j)*(i-j))
        denominator_value += ((i-list1_mean_value)*(i-list1_mean_value))
    nse_value = 1 - (numerator_value/denominator_value)
    nse_value = round(nse_value,6)
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if (len(first_list)==0 or len(second_list)==0):
        return 0
    if(len(first_list) != len(second_list)):
        return 0
    #Calculating the mean value of first list
    summation_value = 0
    for i in first_list:
        if (isinstance(i,(int,float))==False):
            return 0
        else:
            summation_value += i
    mean_value_first = summation_value/len(first_list)
    #Calculating the mean value of second list
    summation_value1 = 0
    for i in second_list:
        if (isinstance(i,(int,float))==False):
            return 0
        else:
            summation_value1 += i
    mean_value_second = summation_value1/len(second_list)
    # Now Calculating the PCC value using mean values of first list and second list
    numerator_part = 0
    denominator_part1 = 0
    denominator_part2 = 0
    for (i,j) in zip(first_list,second_list):
        numerator_part += ((i-mean_value_first)*(j-mean_value_second))
        denominator_part1 += ((i-mean_value_first)*(i-mean_value_first))
        denominator_part2 += ((j-mean_value_second)*(j-mean_value_second))
    pcc_value = (numerator_part)/((math.sqrt(denominator_part1))*(math.sqrt(denominator_part2)))
    pcc_value = round(pcc_value,6)
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    if (len(first_list)==0):
        return 0
    #Calculating the mean value
    summation_value = 0
    for i in first_list:
        if (isinstance(i,(int,float))==False):
            return 0
        else:
            summation_value += i
    mean_value = summation_value/len(first_list)
    # Calculating the standard deviation value through variance
    standard_deviation_value = standard_deviation(first_list)
    # Now Calculating the Skewness value using mean value and standard deviation value
    sum_value = 0
    for i in first_list:
        sum_value += (((i-mean_value)*(i-mean_value)*(i-mean_value))/(standard_deviation_value*standard_deviation_value*standard_deviation_value))
    skewness_value = sum_value/len(first_list)
    skewness_value = round(skewness_value,6)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for i in first_list:
        if (isinstance(i,(int,float))==False):
            return 0
        else:
            summation_value += i
    summation_value = round(summation_value,6)
    return summation_value
