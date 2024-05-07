/* tslint:disable */
/* eslint-disable */
/**
 * chomestatus API
 * The API for chromestatus.com. chromestatus.com is the official tool used for tracking feature launches in Blink (the browser engine that powers Chrome and many other web browsers). This tool guides feature owners through our launch process and serves as a primary source for developer information that then ripples throughout the web developer ecosystem. More details at: https://github.com/GoogleChrome/chromium-dashboard
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { LinkPreviewOpenGraphAllOfInformation } from './LinkPreviewOpenGraphAllOfInformation';
import {
    LinkPreviewOpenGraphAllOfInformationFromJSON,
    LinkPreviewOpenGraphAllOfInformationFromJSONTyped,
    LinkPreviewOpenGraphAllOfInformationToJSON,
} from './LinkPreviewOpenGraphAllOfInformation';

/**
 * 
 * @export
 * @interface LinkPreviewOpenGraph
 */
export interface LinkPreviewOpenGraph {
    /**
     * 
     * @type {string}
     * @memberof LinkPreviewOpenGraph
     */
    url: string;
    /**
     * 
     * @type {string}
     * @memberof LinkPreviewOpenGraph
     */
    type: string;
    /**
     * 
     * @type {LinkPreviewOpenGraphAllOfInformation}
     * @memberof LinkPreviewOpenGraph
     */
    information: LinkPreviewOpenGraphAllOfInformation;
    /**
     * 
     * @type {number}
     * @memberof LinkPreviewOpenGraph
     */
    http_error_code: number;
}

/**
 * Check if a given object implements the LinkPreviewOpenGraph interface.
 */
export function instanceOfLinkPreviewOpenGraph(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "url" in value;
    isInstance = isInstance && "type" in value;
    isInstance = isInstance && "information" in value;
    isInstance = isInstance && "http_error_code" in value;

    return isInstance;
}

export function LinkPreviewOpenGraphFromJSON(json: any): LinkPreviewOpenGraph {
    return LinkPreviewOpenGraphFromJSONTyped(json, false);
}

export function LinkPreviewOpenGraphFromJSONTyped(json: any, ignoreDiscriminator: boolean): LinkPreviewOpenGraph {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'url': json['url'],
        'type': json['type'],
        'information': LinkPreviewOpenGraphAllOfInformationFromJSON(json['information']),
        'http_error_code': json['http_error_code'],
    };
}

export function LinkPreviewOpenGraphToJSON(value?: LinkPreviewOpenGraph | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'url': value.url,
        'type': value.type,
        'information': LinkPreviewOpenGraphAllOfInformationToJSON(value.information),
        'http_error_code': value.http_error_code,
    };
}

