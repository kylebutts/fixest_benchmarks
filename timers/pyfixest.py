import time
import pandas as pd
import pyfixest as pf


def pyfixest_feols_timer(data, fml, vcov=None):
    start_time = time.time()
    _ = pf.feols(fml, data)
    elapsed_time = time.time() - start_time
    return elapsed_time


def pyfixest_fepois_timer(data, fml, vcov=None):
    start_time = time.time()
    _ = pf.fepois(fml, data)
    elapsed_time = time.time() - start_time
    return elapsed_time


def pyfixest_feglm_logit_timer(data, fml, vcov=None):
    start_time = time.time()
    _ = pf.feglm(fml, data, "logit")
    elapsed_time = time.time() - start_time
    return elapsed_time


def pyfixest_feols_multiple_vcov_timer(data, fml, cluster):
    start_time = time.time()
    est = pf.feols(fml, data, vcov="hetero")
    _ = est.vcov(vcov={"CRV1": cluster})
    elapsed_time = time.time() - start_time
    return elapsed_time
