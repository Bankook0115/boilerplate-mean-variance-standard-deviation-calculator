import numpy as np

def calculate(ls):
  result = {}
  #The input of the function should be a list containing 9 digits
  if (len(ls) == 9):
    #convert into 3x3 matrix
      #arr = np.array([ls[0:3],ls[3:6],ls[6:9]]) #quite bad method!
      arr = np.array(ls)
      arr = np.reshape(arr,(3, 3)) #reshape to matrix 3x3
    #long code!
    #find out the output
      '''
      #find mean
      mean_axis1 = np.mean(arr,axis=0).tolist()
      mean_axis2 = np.mean(arr,axis=1).tolist()
      mean_flatten = np.mean(arr).tolist()
      ls_mean = [mean_axis1,mean_axis2,mean_flatten]
      #Find var
      var_axis1 = np.var(arr,axis=0).tolist()
      var_axis2 = np.var(arr,axis=1).tolist()
      var_flatten = np.var(arr).tolist()
      ls_var = [var_axis1,var_axis2,var_flatten]
  
      #Find std
      std_axis1 = np.std(arr,axis=0).tolist()
      std_axis2 = np.std(arr,axis=1).tolist()
      std_flatten = np.std(arr).tolist()
      ls_std = [std_axis1,std_axis2,std_flatten]
      #Find max
      max_axis1 = np.max(arr,axis=0).tolist()
      max_axis2= np.max(arr,axis=1).tolist()
      max_flatten = np.max(arr).tolist()
      ls_max = [max_axis1,max_axis2,max_flatten]
      #Find min
      min_axis1 = np.min(arr,axis=0).tolist()
      min_axis2 = np.min(arr,axis=1).tolist()
      min_flatten = np.min(arr).tolist()
      ls_min = [min_axis1,min_axis2,min_flatten]
  
      #Find sum
      sum_axis1 = np.sum(arr,axis=0).tolist()
      sum_axis2 = np.sum(arr,axis=1).tolist()
      sum_flatten = np.sum(arr).tolist()
      ls_sum = [sum_axis1,sum_axis2,sum_flatten]
      
      print(ls_mean)
      print(ls_var)
      print(ls_std)
      print(ls_max)
      print(ls_min)
      print(ls_sum)
      
  
      #print out the answer
      result['mean'] = ls_mean
      result['variance'] = ls_var
      result['standard deviation'] = ls_std
      result['max'] = ls_max
      result['min'] = ls_min
      result['sum'] = ls_sum
      '''
      #compact code! : refactor
      result = {
        'mean': [np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr).tolist()],
        'variance' : [np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr).tolist()],
        'standard deviation' : [np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr).tolist()],
        'max' : [np.max(arr,axis=0).tolist(),np.max(arr,axis=1).tolist(),np.max(arr).tolist()],
        'min' : [np.min(arr,axis=0).tolist(),np.min(arr,axis=1).tolist(),np.min(arr).tolist()],
        'sum' : [np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr).tolist()]
      }
    
      return result
  else:
    raise ValueError("List must contain nine numbers.")
    return result   