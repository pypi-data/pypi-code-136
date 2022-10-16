        
        
if self.spv_be:
    self.penalty_be[bd] = tf.constant(0.0)
    if (bd in self.beup) or (bdr in self.beup):
        bd_ = bd if bd in self.beup else bdr
        for beup_ in self.beup[bd_]:
            r_,be_u = beup_  
            fu      = tf.where(tf.less_equal(self.rbd[bd],r_),1.0,0.0) ##### 
            pen_e   = tf.reduce_sum(input_tensor=tf.nn.relu((self.EBD[bd] - be_u)*fu))
            self.penalty_be[bd] = self.penalty_be[bd] + pen_e
            
    if (bd in self.belo) or (bdr in self.belo):
        bd_ = bd if bd in self.belo else bdr
        for belo_ in self.belo[bd_]:
            r_,be_l = belo_
            fl      = tf.where(tf.greater(self.rbd[bd],r_),1.0,0.0)   #####
            pen_e   = tf.reduce_sum(input_tensor=tf.nn.relu((be_l - self.EBD[bd])*fl))
            self.penalty_be[bd] = self.penalty_be[bd] + pen_e

    penalty = tf.add(self.penalty_be[bd]*self.lambda_bd,penalty) 



