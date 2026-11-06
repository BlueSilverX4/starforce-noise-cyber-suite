module WaveRoad;

export {
    redef enum Notice::Type += {
        High_Frequency_Wave_Interference
    };
}

event connection_established(c: connection) {
    # Custom baseline tracking logic for rapid connection spikes
    if ( c$duration > 0secs && c$orig$size > 5000000 ) {
        NOTICE([$note=High_Frequency_Wave_Interference,
                $msg=fmt("Wave anomaly detected: Large payload transfer from %s", c$id$orig_h),
                $conn=c]);
    }
}
