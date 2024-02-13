/* SDSS Spectro-Photometry for SDSS Spectroscopic Sample - "Small" Version */

SELECT

    p.objID,p.ra,p.dec,p.raErr,p.decErr,p.type,

    p.dered_u,p.dered_g,p.dered_r,p.dered_i,p.dered_z,

    z.objid as zphot_objid, z.z as zphot, z.zerr as zphot_err,

    s.survey as survey, s.instrument as instrument, s.z as zspec, s.zerr as zspecerr, s.zwarning as zspecwarning, s.class as specclass, s.subclass as specsubclass, s.rChi2 as rChi2, s.DOF$

    p.score
    
    FROM photoobj AS p
    LEFT JOIN photoz AS z ON z.objid = p.objid
    LEFT JOIN specobj AS s ON s.bestobjid = p.objid
    WHERE p.mode = 1 AND p.clean = 1 AND s.zwarning = 0
    
    INTO mydb.sdss_all_small_dr16

/* SDSS Spectro-Photometry & AllWISE Photometry for SDSS Spectroscopic Sample - Small Version */

SELECT
    
    p.objID,p.ra,p.dec,p.raErr,p.decErr,p.type,
    
    p.dered_u,p.dered_g,p.dered_r,p.dered_i,p.dered_z,
    
    z.objid as zphot_objid, z.z as zphot, z.zerr as zphot_err,
    
    s.survey as survey, s.instrument as instrument, s.z as zspec, s.zerr as zspecerr, s.zwarning as zspecwarning, s.class as specclass, s.subclass as specsubclass, s.rChi2 as rChi2, s.DOF$
    
    p.score,x.match_dist,w.cntr,w.w1mpro,w.w2mpro,w.w3mpro,w.w4mpro,w.w1snr,w.w2snr,w.w3snr,w.w4snr,w.blend_ext_flags
    
    FROM photoobj AS p
    LEFT JOIN photoz AS z ON z.objid = p.objid
    LEFT JOIN specobj AS s ON s.bestobjid = p.objid
    LEFT JOIN wise_xmatch AS x ON x.sdss_objid = p.objid
    LEFT JOIN wise_allsky AS w ON w.cntr = dx.wise_cntr
    WHERE p.mode = 1 AND p.clean = 1 AND s.zwarning = 0
    
    INTO mydb.sdss_all_small_dr16_allwise

